CREATE TABLE  "AGENTS" 
(	
	"AGENT_CODE" CHAR(6) NOT NULL PRIMARY KEY, 
	"AGENT_NAME" CHAR(40), 
	"WORKING_AREA" CHAR(35), 
	"COMMISSION" NUMBER(10,2), 
	"PHONE_NO" CHAR(15)
 );


INSERT INTO AGENTS VALUES ('A007', 'Ramasundar', 'Bangalore', '0.15', '077-25814763' );
INSERT INTO AGENTS VALUES ('A003', 'Alex ', 'London', '0.13', '075-12458969');
INSERT INTO AGENTS VALUES ('A008', 'Alford', 'New York', '0.12', '044-25874365');
INSERT INTO AGENTS VALUES ('A011', 'Ravi Kumar', 'Bangalore', '0.15', '077-45625874');
INSERT INTO AGENTS VALUES ('A010', 'Santakumar', 'Chennai', '0.14', '007-22388644');
INSERT INTO AGENTS VALUES ('A012', 'Lucida', 'San Jose', '0.12', '044-52981425');
INSERT INTO AGENTS VALUES ('A005', 'Anderson', 'Brisban', '0.13', '045-21447739');
INSERT INTO AGENTS VALUES ('A001', 'Subbarao', 'Bangalore', '0.14', '077-12346674');
INSERT INTO AGENTS VALUES ('A002', 'Mukesh', 'Mumbai', '0.11', '029-12358964');
INSERT INTO AGENTS VALUES ('A006', 'McDen', 'London', '0.15', '078-22255588');


--1) 핸드폰 번호 중 "123"이 포함된 AGENT_NAME을 출력하시오.
--select Agent_name from agents where PHONE_NO like '%123%';

--2) Commission 0.11 을 받은 사람의 WORKING_AREA를 출력하시오.
-- select working_area from agents where commission = 0.11;

--3) AGENT_CODE 가 'A001'부터 'A008'인 PHONE_NO를 출력하시오.
-- select agent_code, phone_no from agents where agent_code between 'A001' and 'A008'

--4) WORKING_AREA가 'Bangalore' 이거나 COMMISSION 이 0.13 이하인 에이전트을 AGENT_CODE의 내림차순으로 출력하시오.
--select agent_name, commission, agent_code from agents where working_area = 'Bangalore' or commission <= 0.13 order by agent_code desc;

--5) Commission 이 0.12보다 높은 사람 중 이름이 A로 시작되는 AGENT_NAME을 출력하시오.
--select agent_name, commission from agents where commission>0.12 and agent_name like 'A%';