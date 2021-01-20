from flask import Flask, render_template,redirect,url_for,request,session
import mysql.connector



def interact_db(query,query_type: str):
    return_value=False
    connection =mysql.connector.connect(host='localhost',
                                        user='root',password='poipbnm789',database='web_class')
    cursor=connection.cursor(named_tuple=True) #allow you to use .id
    cursor.excute(query)

    if query_type == 'commit':
        #when use insert update delete statement
        connection.commit()
        return_value=True

    if query_type == 'commit':
        # when use insert update delete statement
        query_result=cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return  return_value



User_List={"noam": "student", "tomer": "mailmen", "sharon": "teacher", "amit": "Soccer player"}
query='insert into users values %s '%('("noam","student"),("tomer","mailmen"),("sharon","teacher"),("amit","soccer player")' )
print (query)
interact_db(query, 'commit')