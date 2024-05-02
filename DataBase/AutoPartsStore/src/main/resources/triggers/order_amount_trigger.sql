CREATE OR REPLACE FUNCTION check_item_availability()
    RETURNS TRIGGER AS $$
DECLARE
    available_amount INTEGER;
BEGIN
    -- �������� ��������� ���������� ������� �� ������
    SELECT amount INTO available_amount
    FROM item
    WHERE item_id = NEW.item_id;

    -- ���������, ���������� �� ������� �� ������ ��� ������
    IF available_amount < NEW.amount THEN
        RAISE EXCEPTION '������������ ������� �� ������ ��� ������';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER item_availability_check
    BEFORE INSERT ON order_list
    FOR EACH ROW
EXECUTE FUNCTION check_item_availability();
