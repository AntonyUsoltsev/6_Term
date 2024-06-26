import React, {useEffect, useState} from "react";
import {Form, Button, Table, Input, Popconfirm, message, Modal} from "antd";
import PostService from "../../postService/PostService";

const SupplierTypeEdit: React.FC = () => {
    const [supplierTypesData, setSupplierTypesData] = useState([]);
    const [isModalVisible, setIsModalVisible] = useState(false);
    const [editMode, setEditMode] = useState(false);
    const [typeName, setTypeName] = useState("");
    const [selectedSupplierTypeId, setSelectedSupplierTypeId] = useState(null);
    const [form] = Form.useForm();

    useEffect(() => {
        fetchSupplierTypes();
    }, []);

    const fetchSupplierTypes = () => {
        PostService.getRequest(`supplierType/all`).then((response: any) => {
            setSupplierTypesData(response.data);
        });
    };

    const handleSave = async () => {
        try {
            const body = {
                typeName: typeName,
            }
            if (editMode) {
                await PostService.updateRequest(`supplierType/${selectedSupplierTypeId}`, body);
            } else {
                await PostService.addRequest(`supplierType`, body);
            }
            fetchSupplierTypes();
            resetForm();
        } catch (error) {
            message.error("Failed to save the supplier type.");
        }
    };

    const handleDelete = async (supplierTypeId: number) => {
        try {
            await PostService.deleteRequest(`supplierType/${supplierTypeId}`).then((response: any) => {
                fetchSupplierTypes();
            });

        } catch (error) {
            message.error("Failed to delete the supplier type.");
        }
    };

    const resetForm = () => {
        setEditMode(false);
        setTypeName("");
        setSelectedSupplierTypeId(null);
        setIsModalVisible(false);
    };

    const columns = [
        {
            title: "Тип поставщика",
            dataIndex: "typeName",
            key: "typeName",
        },
        {
            title: "Действия",
            key: "actions",
            render: (text: any, record: any) => (
                <span>
                    <a onClick={() => {
                        setEditMode(true);
                        setTypeName(record.typeName);
                        setSelectedSupplierTypeId(record.typeId);
                        setIsModalVisible(true);
                    }}>Редактировать</a>
                    <Popconfirm
                        title="Вы уверены, что хотите удалить этот тип поставщика?"
                        onConfirm={() => handleDelete(record.typeId)}
                        okText="Да"
                        cancelText="Нет"
                    >
                        <a style={{marginLeft: 8}}>Удалить</a>
                    </Popconfirm>
                </span>
            ),
        },
    ];
    const handleAdd = () => {
        setEditMode(false);
        setTypeName("");
        setSelectedSupplierTypeId(null);
        setIsModalVisible(true);
    };

    return (
        <div>
            <h2 style={{marginBottom: "15px"}}>Категории поставщиков</h2>
            <Button type="primary" onClick={handleAdd}>
                Добавить
            </Button>
            <Table columns={columns} dataSource={supplierTypesData}/>
            <Modal
                title={editMode ? "Редактировать тип поставщика" : "Добавить тип поставщика"}
                visible={isModalVisible}
                onOk={handleSave}
                onCancel={resetForm}
                okText={editMode ? "Сохранить" : "Добавить"}
                cancelText="Отмена"
            >
                <Form form={form} layout="vertical">
                    <Form.Item
                        label="Тип поставщика"
                        rules={[{required: true, message: "Пожалуйста, введите тип"}]}
                    >
                        <Input value={typeName} onChange={(e) => setTypeName(e.target.value)}/>
                    </Form.Item>
                </Form>
            </Modal>
        </div>
    );
};

export default SupplierTypeEdit;
