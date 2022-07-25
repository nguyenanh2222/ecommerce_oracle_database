 
CREATE SEQUENCE ORDER_ITEM_SEQ START WITH 1;
CREATE SEQUENCE SKU_SEQ START WITH 1;
CREATE SEQUENCE PRODUCT_SEQ START WITH 1;
CREATE SEQUENCE CATEGORY_SEQ START WITH 1;
CREATE SEQUENCE TBL_ORDER_SEQ START WITH 1;
CREATE SEQUENCE CART_ITEM_SEQ START WITH 1;

CREATE OR REPLACE TRIGGER ORDER_ITEM_INSERT
    BEFORE INSERT
    ON ORDER_ITEM
    FOR EACH ROW
BEGIN
    SELECT ORDER_ITEM_SEQ.nextval
    INTO :new.ID
    FROM dual;
        
CREATE OR REPLACE TRIGGER SKU_INSERT
    BEFORE INSERT
    ON SKU
    FOR EACH ROW
BEGIN
    SELECT SKU_SEQ.nextval
    INTO :new.ID
    FROM dual;
        
CREATE OR REPLACE TRIGGER PRODUCT_INSERT
    BEFORE INSERT
    ON PRODUCT
    FOR EACH ROW
BEGIN
    SELECT PRODUCT_SEQ.nextval
    INTO :new.ID
    FROM dual;
        
CREATE OR REPLACE TRIGGER CATEGORY_INSERT
    BEFORE INSERT
    ON CATEGORY
    FOR EACH ROW
BEGIN
    SELECT CATEGORY_SEQ.nextval
    INTO :new.ID
    FROM dual;
        
CREATE OR REPLACE TRIGGER TBL_ORDER_INSERT
    BEFORE INSERT
    ON TBL_ORDER
    FOR EACH ROW
BEGIN
    SELECT TBL_ORDER_SEQ.nextval
    INTO :new.ID
    FROM dual;
        
CREATE OR REPLACE TRIGGER CART_ITEM_INSERT
    BEFORE INSERT
    ON CART_ITEM
    FOR EACH ROW
BEGIN
    SELECT CART_ITEM_SEQ.nextval
    INTO :new.ID
    FROM dual;
        

Process finished with exit code 0
