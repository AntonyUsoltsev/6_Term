import React, {useState} from "react";
import {Form, Input, Button, Table} from "antd";
import PostService from "../../postService/PostService";

const CustomerByItemWithAmountQuery = () => {
    const [form] = Form.useForm();
    const [activeQuery, setActiveQuery] = useState<boolean>(false);
    const [customerData, setCustomerData] = useState<[]>([]);

    const handleSubmit = (values: any) => {
        setActiveQuery(true);
        const {startDate, endDate, amount, itemName} = values;

        // Получение данных
        PostService.getCustomerByItemWithAmount(startDate, endDate, amount, itemName).then(
            (response: any) => {
                setCustomerData(response.data);
            }
        );
    };

    const columns = [
        {
            title: "Имя",
            dataIndex: "name",
            key: "name",
        },
        {
            title: "Фамилия",
            dataIndex: "secondName",
            key: "secondName",
        },
        {
            title: "Email",
            dataIndex: "email",
            key: "email",
        },
    ];

    return (
        <div>
            <Form name="getSuppliers" onFinish={handleSubmit} form={form}>
                <Form.Item
                    name="startDate"
                    rules={[{required: true, message: "Введите дату начала"}]}
                >
                    <Input placeholder="Введите дату начала в формате YYYY-MM-DD hh:mm:ss"/>
                </Form.Item>
                <Form.Item
                    name="endDate"
                    rules={[{required: true, message: "Введите дату конца"}]}
                >
                    <Input placeholder="Введите дату конца в формате YYYY-MM-DD hh:mm:ss"/>
                </Form.Item>
                <Form.Item
                    name="itemName"
                    rules={[{required: true, message: "Введите название детали"}]}
                >
                    <Input placeholder="Введите название детали "/>
                </Form.Item>
                <Form.Item
                    name="amount"
                    rules={[{required: true, message: "Введите количество"}]}
                >
                    <Input placeholder="Введите количество"/>
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit">
                        Получить список покупателей
                    </Button>
                </Form.Item>
            </Form>
            <div style={{display: activeQuery ? "block" : "none"}}>
                <h2 style={{marginBottom: "15px"}}>Поставщики</h2>
                <Table columns={columns} dataSource={customerData}/>
            </div>
        </div>
    );
};

export default CustomerByItemWithAmountQuery;
