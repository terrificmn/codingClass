from streamlit.elements import number_input
from DbModel import DbModel
import streamlit as st
from mysql.connector import Error
import pandas as pd
import re

class SqlController (DbModel) :
    # def __init__ (self):
    #     pass
    #     self.validationType = 
 
    def validation(self, title, author_lname, author_fname ,released_year, stock_quantity, pages):
        name_regex = '^[a-zA-Z가-힣]+$'
        #number_regex = '^[0-9]+$'
        #email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        number_info = "숫자만 입력 가능합니다"

        # 공백 제거
        title = title.strip(' ')
        author_lname = author_lname.strip(' ')
        author_fname = author_fname.strip(' ')

        if len(author_lname) == 0 or len(author_fname) == 0 or len(title) == 0 :
            st.error('입력해주세요')
            return False
        
        elif not re.search(name_regex, author_lname) :
            st.error('이름은 숫자 입력은 불가능 합니다.')
            return False

        elif not re.search(name_regex, author_fname) :
            st.error('이름은 숫자 입력은 불가능 합니다.')
            return False
        
            
        elif released_year == 0   : # 스트림릿은 number_input은 문자로 입력하면 0 을 넘김
            st.error('출판 년도는 ' + number_info)
            return False

        elif stock_quantity == 0 :
            st.error('재고량은 '  + number_info)
            return False

        elif pages == 0 :
            st.error('페이지수는 ' + number_info)
            return False

        # elif not re.search(released_year, number_regex) :
        #     st.error('숫자만 입력 가능합니다.')
        # elif(not re.search(email_regex, email)):  
        #     st.error("Email 형식을 확인해 주세요!") 
        #     return False
        else :
            # 마지막 최종적으로 통과시에 True 리턴
            return True

    

    # book_id, amendTitle, amendLastname, amendFirstname, amendYear, amendQuantity, amendPages
    def update_validation(self, book_id, title, author_lname, author_fname, released_year, stock_quantity, pagaes):
        
        #print(book_id, title, author_lname, author_fname, released_year, stock_quantity, pagaes)
        name_regex = '^[a-zA-Z가-힣]+$'
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        # 공백 제거
        title = title.strip(' ')
        author_lname = author_lname.strip(' ')
        author_fname = author_fname.strip(' ')
        if len(title) == 0:
            st.error('바꿀 책 이름을 입력해주세요')
            return False
        elif len(author_lname) == 0:
            st.error('바꿀 성을 입력해주세요')
            return False
        elif len(author_fname) == 0:
            st.error('바꿀 이름을 입력해주세요')
            return False
        else :
            # sql_update() 메소드에서 사용하기 위해서 book_id를 맨 뒤로 (튜플로)
            return title, author_fname, author_lname, released_year, stock_quantity, pagaes, book_id



    def sql_select(self, chosenColumns, table, limit):
        # chosenColumns 은 리스트형식, limit은 int
        if len(chosenColumns) > 0 :
            selectedColumn = ", ".join(chosenColumns)
        else :
            st.warning('한개 이상의 컬럼을 선택을 해주세요')
            return False
        
        conn = self.dbConnection()
        cursor = conn.cursor(dictionary=True)

        query = " SELECT " + selectedColumn + " FROM " + table + " ORDER by book_id DESC LIMIT %s ; "
        #st.write(type(limit))
        data = (limit, )
        cursor.execute(query, data) #  쿼리 실행
        results = cursor.fetchall()   
        cursor.close()
        conn.close()
        #json_results = json.dumps(results)
        return results
        
        



    def sql_update(self, updateData):
        conn = self.dbConnection()
        cursor = conn.cursor(dictionary=True)

        query = """UPDATE books SET title = %s, author_fname = %s, 
                    author_lname = %s, released_year = %s, stock_quantity = %s, pages = %s
                    WHERE book_id = %s; """

        #print(updateData)

        try:
            cursor.execute(query, updateData)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print('디비 관련 에러 발생', e)
        finally:
            print('에러가 없으면 update성공!')




    def sql_insert(self, title, author_lname, author_fname, released_year, stock_quantity, pagaes ):
        # 연결
        
        conn = self.dbConnection()
        cursor = conn.cursor(dictionary=True)
        
        query = """INSERT INTO books 
                    (title, author_fname, author_lname, released_year, stock_quantity, pages)
                    VALUES (%s, %s, %s, %s, %s, %s); """ 
        value_data = (title, author_fname, author_lname, released_year, stock_quantity, pagaes) # 튜플로 만든다
        #print(value_data)
        try:
            cursor.execute(query, value_data)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print('디비 관련 에러 발생', e)
        finally:
            print('에러가 없으면 insert성공!!')



    def sql_delete(self, book_id):
        conn = self.dbConnection()
        cursor = conn.cursor(dictionary=True)

        query = """ DELETE FROM books
                    WHERE book_id = %s """
        row = (book_id, )

        try:
            cursor.execute(query, row)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print('디비 관련 에러 발생', e)
        finally:
            print('에러가 없으면 insert성공!!')

