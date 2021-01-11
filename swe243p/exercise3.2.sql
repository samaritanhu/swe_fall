# Problem 1
USE ap;
CREATE INDEX vendors_zip_code_ix ON vendors (vendor_zip_code);

# Problem 2
USE ex;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS committees;
DROP TABLE IF EXISTS members_committees;

CREATE TABLE members (
member_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
address VARCHAR(200) NOT NULL,
city VARCHAR(45) NOT NULL,
state VARCHAR(45) NOT NULL,
phone VARCHAR(20) NOT NULL
);

CREATE TABLE committees (
committee_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
committee_name VARCHAR(200) NOT NULL
);

CREATE TABLE members_committees (
member_id INT NOT NULL,
committee_id INT NOT NULL,
CONSTRAINT members_committees_fk_members FOREIGN KEY (member_id)
REFERENCES members (member_id), 
CONSTRAINT members_committes_fk_committees FOREIGN KEY (committee_id)
REFERENCES committees (committee_id)
);

# Problem 3
USE ex;
INSERT INTO members
VALUES
(DEFAULT, "Xinyi", "Hu", "260 Aldrich Hall", "Irvine", "CA", "(949) 824-5011"),
(DEFAULT, "Nobody", "Who", "Nowhere", "Irvine", "CA", "(111) 111-1111");

INSERT INTO committees 
VALUES 
(DEFAULT, "UC Irvine"),
(DEFAULT, "No One");

INSERT INTO members_committees 
VALUES
(1, 2),
(1, 1),
(2, 1);

SELECT committee_name, last_name, first_name
FROM 
members 
JOIN members_committees
ON members.member_id = members_committees.member_id
JOIN committees
ON members_committees.committee_id = committees.committee_id
ORDER BY committee_name, last_name, first_name;

# Problem 4
ALTER TABLE members 
ADD annual_dues DECIMAL(5,2) DEFAULT 52.50;

ALTER TABLE members 
ADD payment_date DATE; 

# Problem 5
ALTER TABLE committees
MODIFY committee_name VARCHAR(200) NOT NULL UNIQUE;

INSERT INTO committees 
VALUES 
(DEFAULT, "UC Irvine");
