import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

loc = sys.argv[1]
lang = sys.argv[2]
plang = sys.argv[3]
job = sys.argv[4]
user_name = sys.argv[5]

# Mentor data with name, email, and birthday
mentors_data = [
    { 
                    "name": "Pham Ngoc Long", 
                    "email": "pnlong27@gmail.com",
                    "birthday": "2004-06-27",
                    "characteristic": "hardworking",
                    "hobbies": "coding, book",
                    "addInf": "",
                    "loc": "Hue, Viet Nam",
                    "lang": "Vietnamese",
                    "p_lang": "c",
                    "job": "ai-data"
                },
{
        "name": "Nguyen Anh Khiem",
        "email": "pqr@gmail.com",
        "birthday": "2005-01-01",
        "characteristic": "hardworking",
        "hobbies": "badminton, book, baseball",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese, English",
        "p_lang": "c++, java, c",
        "job": "android"
    },

{
        "name": "Do Thanh Kien",
        "email": "jkl@gmail.com",
        "birthday": "1997-03-17",
        "characteristic": "shy, lazy",
        "hobbies": "coding",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "golang, c",
        "job": "front-end"
    },

{
        "name": "Do Phuong Minh Hieu",
        "email": "pqr@gmail.com",
        "birthday": "2004-02-17",
        "characteristic": "polite, carefree, hardworking",
        "hobbies": "baseball, running, coding",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "golang, sql",
        "job": "android"
    },

{
        "name": "Nguyen Sy Minh",
        "email": "def@gmail.com",
        "birthday": "1998-04-20",
        "characteristic": "hardworking",
        "hobbies": "book, badminton",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "rust, java",
        "job": "ai-data"
    },

{
        "name": "Tao Van Long",
        "email": "mno@gmail.com",
        "birthday": "1999-10-16",
        "characteristic": "intelligent, shy",
        "hobbies": "badminton, baseball",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, English, Korean",
        "p_lang": "rust, java",
        "job": "cyber"
    },

{
        "name": "Tran Van Hieu",
        "email": "pqr@gmail.com",
        "birthday": "1995-09-10",
        "characteristic": "selfish",
        "hobbies": "book, badminton, running",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "sql",
        "job": "fullstack"
    },

{
        "name": "Dao Thanh Hieu",
        "email": "mno@gmail.com",
        "birthday": "1990-12-15",
        "characteristic": "considerate",
        "hobbies": "baseball, game, running",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "python",
        "job": "front-end"
    },

{
        "name": "Dao Cong Vu",
        "email": "ghi@gmail.com",
        "birthday": "2000-04-10",
        "characteristic": "lazy, creative, humor",
        "hobbies": "baseball",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "sql, golang, c++",
        "job": "devops"
    },

{
        "name": "Ha Sy Cong",
        "email": "pqr@gmail.com",
        "birthday": "1990-06-28",
        "characteristic": "lazy, selfish",
        "hobbies": "badminton, coding, running",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Chinese, Korean",
        "p_lang": "c, python",
        "job": "student"
    },

{
        "name": "Tran Kim Thanh Nhat",
        "email": "pqr@gmail.com",
        "birthday": "1994-01-24",
        "characteristic": "intelligent, selfish",
        "hobbies": "badminton, book, coding",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "rust, sql",
        "job": "ai-data"
    },

    {
        "name": "Vu Trong Nam",
        "email": "jkl@gmail.com",
        "birthday": "1996-05-26",
        "characteristic": "creative",
        "hobbies": "game, badminton",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, English, Korean",
        "p_lang": "c++, python, java",
        "job": "cyber"
    },

    {
        "name": "Dao Kim Thanh Nhat",
        "email": "abc@gmail.com",
        "birthday": "2004-03-07",
        "characteristic": "hardworking, polite, jealous",
        "hobbies": "book, game, running",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "javascript",
        "job": "fullstack"
    },

    {
        "name": "Trinh Dac Cong",
        "email": "ghi@gmail.com",
        "birthday": "1999-06-07",
        "characteristic": "humor",
        "hobbies": "book, running",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "javascript, c, golang",
        "job": "ios"
    },

    {
        "name": "Le Thanh Nhat",
        "email": "ghi@gmail.com",
        "birthday": "2001-11-16",
        "characteristic": "hardworking, considerate, creative",
        "hobbies": "running",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "c, rust",
        "job": "android"
    },

    {
        "name": "Dao Anh Cuong",
        "email": "pqr@gmail.com",
        "birthday": "2004-09-28",
        "characteristic": "jealous, selfish, humor",
        "hobbies": "game, book, badminton",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "python, rust",
        "job": "back-end"
    },

    {
        "name": "Do Anh Kien",
        "email": "ghi@gmail.com",
        "birthday": "2000-11-16",
        "characteristic": "humor",
        "hobbies": "badminton, baseball, running",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "c, rust",
        "job": "game"
    },

    {
        "name": "Do Song Khiem",
        "email": "abc@gmail.com",
        "birthday": "2001-10-08",
        "characteristic": "rude, humor, quite",
        "hobbies": "book",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese, Chinese, Korean",
        "p_lang": "golang, c++",
        "job": "front-end"
    },

    {
        "name": "Ha Trong Kien",
        "email": "mno@gmail.com",
        "birthday": "2004-04-27",
        "characteristic": "carefree, quite",
        "hobbies": "coding, game",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "python",
        "job": "android"
    },

    {
        "name": "Tao Sy Viet",
        "email": "abc@gmail.com",
        "birthday": "1992-12-07",
        "characteristic": "shy, humor, creative",
        "hobbies": "book, badminton",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "python, rust, c",
        "job": "student"
    },

    {
        "name": "Vo Phuong Minh Khiem",
        "email": "def@gmail.com",
        "birthday": "1994-05-31",
        "characteristic": "polite",
        "hobbies": "book, badminton",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "sql, c, javascript",
        "job": "back-end"
    },

    {
        "name": "Dao Sy Long",
        "email": "jkl@gmail.com",
        "birthday": "2001-02-26",
        "characteristic": "humor",
        "hobbies": "book",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese, English",
        "p_lang": "sql, c++, python",
        "job": "devops"
    },

    {
        "name": "Nguyen Van Cuong",
        "email": "abc@gmail.com",
        "birthday": "2001-03-09",
        "characteristic": "carefree",
        "hobbies": "running, baseball",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "sql, python",
        "job": "fullstack"
    },

    {
        "name": "Vo Phuong Minh Vu",
        "email": "def@gmail.com",
        "birthday": "1995-01-06",
        "characteristic": "considerate, shy",
        "hobbies": "baseball",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "java, c, sql",
        "job": "student"
    },

    {
        "name": "Trinh Dac Kien",
        "email": "jkl@gmail.com",
        "birthday": "1993-07-17",
        "characteristic": "polite, jealous, quite",
        "hobbies": "baseball",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese, English",
        "p_lang": "golang",
        "job": "android"
    },

    {
        "name": "Vo Sy Kien",
        "email": "abc@gmail.com",
        "birthday": "1998-12-13",
        "characteristic": "intelligent",
        "hobbies": "book",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "rust, java, c",
        "job": "ios"
    },

    {
        "name": "Ha Song Khiem",
        "email": "mno@gmail.com",
        "birthday": "1996-05-08",
        "characteristic": "humor, jealous",
        "hobbies": "running, coding, baseball",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, English",
        "p_lang": "rust, c++",
        "job": "devops"
    },

    {
        "name": "Dao Van Long",
        "email": "def@gmail.com",
        "birthday": "2005-02-18",
        "characteristic": "quite, lazy, humor",
        "hobbies": "game, running, badminton",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "rust",
        "job": "student"
    },

    {
        "name": "Tran Van Cong",
        "email": "jkl@gmail.com",
        "birthday": "2003-02-21",
        "characteristic": "polite",
        "hobbies": "coding",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "javascript",
        "job": "ios"
    },

    {
        "name": "Do Dac Nam",
        "email": "mno@gmail.com",
        "birthday": "1992-05-18",
        "characteristic": "selfish, shy, quite",
        "hobbies": "baseball, book",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese, English",
        "p_lang": "c++, sql",
        "job": "front-end"
    },

    {
        "name": "Vo Kim Thanh Long",
        "email": "jkl@gmail.com",
        "birthday": "1998-09-01",
        "characteristic": "humor, considerate",
        "hobbies": "game, badminton",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Chinese, Korean",
        "p_lang": "golang, python",
        "job": "back-end"
    },

    {
        "name": "Nguyen Dac Minh",
        "email": "ghi@gmail.com",
        "birthday": "1992-09-27",
        "characteristic": "humor",
        "hobbies": "running, book",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "sql, golang",
        "job": "cyber"
    },

    {
        "name": "Pham Cong Cuong",
        "email": "def@gmail.com",
        "birthday": "2003-03-16",
        "characteristic": "considerate, polite, shy",
        "hobbies": "running",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "java",
        "job": "game"
    },

    {
        "name": "Tao Thanh Nam",
        "email": "pqr@gmail.com",
        "birthday": "1998-08-27",
        "characteristic": "rude, considerate, jealous",
        "hobbies": "badminton, baseball, book",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "python",
        "job": "game"
    },

    {
        "name": "Trinh Kim Thanh Kien",
        "email": "ghi@gmail.com",
        "birthday": "1991-08-12",
        "characteristic": "hardworking",
        "hobbies": "badminton, book",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "rust",
        "job": "student"
    },

    {
        "name": "Vu Song Kien",
        "email": "mno@gmail.com",
        "birthday": "1993-06-05",
        "characteristic": "quite, jealous",
        "hobbies": "badminton, book, coding",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese, Korean, English",
        "p_lang": "rust, golang",
        "job": "ios"
    },

    {
        "name": "Vo Dac Nhat",
        "email": "def@gmail.com",
        "birthday": "2003-08-04",
        "characteristic": "intelligent, shy, humor",
        "hobbies": "badminton, baseball",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "golang, javascript",
        "job": "cyber"
    },

    {
        "name": "Pham Thanh Minh",
        "email": "mno@gmail.com",
        "birthday": "1999-03-26",
        "characteristic": "carefree, humor",
        "hobbies": "book, baseball, game",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "golang",
        "job": "fullstack"
    },

    {
        "name": "Trinh Sy Long",
        "email": "mno@gmail.com",
        "birthday": "2005-01-16",
        "characteristic": "quite, humor, intelligent",
        "hobbies": "badminton",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "python, javascript",
        "job": "ios"
    },

    {
        "name": "Tran Cong Hieu",
        "email": "pqr@gmail.com",
        "birthday": "1997-09-07",
        "characteristic": "hardworking",
        "hobbies": "baseball, book",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, Chinese, Korean",
        "p_lang": "golang, c++",
        "job": "devops"
    },

    {
        "name": "Ha Kim Thanh Kien",
        "email": "jkl@gmail.com",
        "birthday": "1998-05-16",
        "characteristic": "selfish, quite, jealous",
        "hobbies": "badminton, baseball",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "c",
        "job": "game"
    },

    {
        "name": "Dao Sy Cuong",
        "email": "mno@gmail.com",
        "birthday": "2000-01-09",
        "characteristic": "carefree, polite, hardworking",
        "hobbies": "coding, running, game",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "c++, rust",
        "job": "back-end"
    },

    {
        "name": "Nguyen Thanh Cong",
        "email": "def@gmail.com",
        "birthday": "1992-03-06",
        "characteristic": "rude",
        "hobbies": "game, badminton",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "javascript",
        "job": "android"
    },

    {
        "name": "Vo Dac Nhat",
        "email": "mno@gmail.com",
        "birthday": "2003-02-11",
        "characteristic": "jealous, humor, hardworking",
        "hobbies": "game",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, English",
        "p_lang": "python, c, sql",
        "job": "student"
    },

    {
        "name": "Nguyen Kim Thanh Nam",
        "email": "jkl@gmail.com",
        "birthday": "2005-02-22",
        "characteristic": "hardworking",
        "hobbies": "badminton, baseball",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese, English, Korean",
        "p_lang": "javascript, java",
        "job": "devops"
    },

    {
        "name": "Vo Dac Minh",
        "email": "abc@gmail.com",
        "birthday": "2001-09-14",
        "characteristic": "polite",
        "hobbies": "running",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "sql, c++, rust",
        "job": "android"
    },

    {
        "name": "Tran Dac Vu",
        "email": "def@gmail.com",
        "birthday": "1991-09-27",
        "characteristic": "considerate, selfish",
        "hobbies": "badminton",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "c",
        "job": "back-end"
    },

    {
        "name": "Nguyen Van Nhat",
        "email": "pqr@gmail.com",
        "birthday": "1999-04-14",
        "characteristic": "hardworking, rude, quite",
        "hobbies": "badminton, baseball, running",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese, English",
        "p_lang": "java",
        "job": "game"
    },

    {
        "name": "Nguyen Sy Nhat",
        "email": "jkl@gmail.com",
        "birthday": "1998-10-02",
        "characteristic": "jealous, quite, carefree",
        "hobbies": "running, baseball, badminton",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese, Chinese, Korean",
        "p_lang": "sql, javascript, c",
        "job": "devops"
    },

    {
        "name": "Vu Minh Vu",
        "email": "jkl@gmail.com",
        "birthday": "1992-11-27",
        "characteristic": "considerate",
        "hobbies": "book, game",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "golang, python",
        "job": "cyber"
    },

    {
        "name": "Tao Phuong Minh Cuong",
        "email": "mno@gmail.com",
        "birthday": "2002-06-08",
        "characteristic": "selfish",
        "hobbies": "badminton, game, book",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, Chinese, English",
        "p_lang": "python, golang",
        "job": "ai-data"
    },

    {
        "name": "Trinh Dac Minh",
        "email": "jkl@gmail.com",
        "birthday": "1995-09-19",
        "characteristic": "humor",
        "hobbies": "baseball, badminton, book",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "javascript, python, c++",
        "job": "back-end"
    },

    {
        "name": "Pham Kim Thanh Minh",
        "email": "mno@gmail.com",
        "birthday": "1992-01-11",
        "characteristic": "jealous, considerate",
        "hobbies": "game, running",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "golang, rust",
        "job": "ai-data"
    },

    {
        "name": "Dao Phuong Minh Cuong",
        "email": "abc@gmail.com",
        "birthday": "2000-06-21",
        "characteristic": "considerate",
        "hobbies": "running, coding, game",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese, Chinese, English",
        "p_lang": "golang",
        "job": "front-end"
    },

    {
        "name": "Tran Trong Nhat",
        "email": "abc@gmail.com",
        "birthday": "2000-10-04",
        "characteristic": "creative, considerate, rude",
        "hobbies": "book, coding, baseball",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese, English, Chinese",
        "p_lang": "java, c++",
        "job": "ai-data"
    },

    {
        "name": "Tao Kim Thanh Hieu",
        "email": "ghi@gmail.com",
        "birthday": "2005-04-13",
        "characteristic": "humor, hardworking",
        "hobbies": "running",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "golang",
        "job": "front-end"
    },

    {
        "name": "Tran Anh Viet",
        "email": "def@gmail.com",
        "birthday": "1994-02-08",
        "characteristic": "lazy, carefree, intelligent",
        "hobbies": "game",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "python",
        "job": "android"
    },

    {
        "name": "Trinh Song Khiem",
        "email": "abc@gmail.com",
        "birthday": "2004-03-06",
        "characteristic": "lazy, quite",
        "hobbies": "game",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "javascript",
        "job": "ios"
    },

    {
        "name": "Dao Cong Vu",
        "email": "ghi@gmail.com",
        "birthday": "2000-07-09",
        "characteristic": "considerate",
        "hobbies": "game, badminton",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese, English, Chinese",
        "p_lang": "sql, c",
        "job": "front-end"
    },

    {
        "name": "Tran Thanh Vu",
        "email": "pqr@gmail.com",
        "birthday": "2000-10-07",
        "characteristic": "lazy, quite, polite",
        "hobbies": "baseball, book, running",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "python, rust",
        "job": "ios"
    },

    {
        "name": "Bui Song Hieu",
        "email": "mno@gmail.com",
        "birthday": "1997-09-12",
        "characteristic": "quite",
        "hobbies": "badminton, game, coding",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "rust, sql",
        "job": "cyber"
    },

    {
        "name": "Le Trong Nam",
        "email": "pqr@gmail.com",
        "birthday": "1999-11-30",
        "characteristic": "creative, jealous",
        "hobbies": "running",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "python",
        "job": "ios"
    },

    {
        "name": "Do Kim Thanh Kien",
        "email": "pqr@gmail.com",
        "birthday": "1997-09-01",
        "characteristic": "creative, selfish, hardworking",
        "hobbies": "running, badminton",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "c++",
        "job": "ios"
    },

    {
        "name": "Trinh Song Kien",
        "email": "pqr@gmail.com",
        "birthday": "1998-01-07",
        "characteristic": "jealous, hardworking",
        "hobbies": "game",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "c, golang",
        "job": "devops"
    },

    {
        "name": "Do Thanh Nam",
        "email": "jkl@gmail.com",
        "birthday": "1992-09-27",
        "characteristic": "intelligent, considerate, lazy",
        "hobbies": "game",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "c++",
        "job": "ai-data"
    },

    {
        "name": "Dao Thanh Long",
        "email": "ghi@gmail.com",
        "birthday": "1993-11-30",
        "characteristic": "intelligent, creative",
        "hobbies": "badminton",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "sql, c, javascript",
        "job": "front-end"
    },

    {
        "name": "Vo Dac Vu",
        "email": "abc@gmail.com",
        "birthday": "2001-09-24",
        "characteristic": "rude, humor, selfish",
        "hobbies": "badminton",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese, English, Korean",
        "p_lang": "java, c",
        "job": "cyber"
    },

    {
        "name": "Nguyen Trong Viet",
        "email": "jkl@gmail.com",
        "birthday": "2002-09-27",
        "characteristic": "rude, considerate",
        "hobbies": "baseball, running",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "java",
        "job": "fullstack"
    },

    {
        "name": "Do Cong Viet",
        "email": "pqr@gmail.com",
        "birthday": "2003-12-26",
        "characteristic": "quite, intelligent",
        "hobbies": "badminton, coding",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "c, golang",
        "job": "cyber"
    },

    {
        "name": "Trinh Dac Nhat",
        "email": "pqr@gmail.com",
        "birthday": "1992-04-28",
        "characteristic": "polite, selfish, lazy",
        "hobbies": "baseball",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "rust, golang",
        "job": "devops"
    },

    {
        "name": "Dao Van Hieu",
        "email": "pqr@gmail.com",
        "birthday": "1996-09-07",
        "characteristic": "selfish",
        "hobbies": "baseball, running, book",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "rust, c++, sql",
        "job": "game"
    },

    {
        "name": "Nguyen Dac Minh",
        "email": "ghi@gmail.com",
        "birthday": "1990-03-04",
        "characteristic": "lazy, considerate, creative",
        "hobbies": "badminton, running, book",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Chinese, Korean",
        "p_lang": "java",
        "job": "android"
    },

    {
        "name": "Bui Anh Viet",
        "email": "def@gmail.com",
        "birthday": "1993-01-03",
        "characteristic": "creative, intelligent",
        "hobbies": "coding",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "c, javascript",
        "job": "fullstack"
    },

    {
        "name": "Do Van Kien",
        "email": "def@gmail.com",
        "birthday": "1990-08-14",
        "characteristic": "lazy, selfish, intelligent",
        "hobbies": "badminton",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "c++",
        "job": "game"
    },

    {
        "name": "Tran Van Hieu",
        "email": "jkl@gmail.com",
        "birthday": "2004-02-05",
        "characteristic": "polite, lazy",
        "hobbies": "book",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "sql, java, c",
        "job": "devops"
    },

    {
        "name": "Vu Phuong Minh Nam",
        "email": "pqr@gmail.com",
        "birthday": "1997-02-16",
        "characteristic": "creative",
        "hobbies": "book, game, baseball",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "javascript, rust, sql",
        "job": "front-end"
    },

    {
        "name": "Dao Cong Vu",
        "email": "jkl@gmail.com",
        "birthday": "2000-05-02",
        "characteristic": "considerate, creative, intelligent",
        "hobbies": "baseball",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "java, c, python",
        "job": "devops"
    },

    {
        "name": "Dao Anh Minh",
        "email": "pqr@gmail.com",
        "birthday": "1996-08-03",
        "characteristic": "considerate, jealous, creative",
        "hobbies": "running, coding, baseball",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "java",
        "job": "ios"
    },

    {
        "name": "Nguyen Trong Nam",
        "email": "pqr@gmail.com",
        "birthday": "2005-08-23",
        "characteristic": "considerate",
        "hobbies": "book, coding",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "c, python, java",
        "job": "cyber"
    },

    {
        "name": "Le Van Cuong",
        "email": "def@gmail.com",
        "birthday": "2001-04-08",
        "characteristic": "shy, quite",
        "hobbies": "game, running",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese, Korean, English",
        "p_lang": "javascript",
        "job": "fullstack"
    },

    {
        "name": "Bui Van Cuong",
        "email": "ghi@gmail.com",
        "birthday": "2003-03-16",
        "characteristic": "humor, carefree",
        "hobbies": "running, baseball, badminton",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese, Korean",
        "p_lang": "c++, sql",
        "job": "game"
    },

    {
        "name": "Bui Phuong Minh Nam",
        "email": "jkl@gmail.com",
        "birthday": "1997-06-06",
        "characteristic": "intelligent, shy, jealous",
        "hobbies": "book, badminton, baseball",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese, Chinese",
        "p_lang": "java, rust",
        "job": "game"
    },

    {
        "name": "Vu Thanh Viet",
        "email": "def@gmail.com",
        "birthday": "2002-01-05",
        "characteristic": "jealous, carefree",
        "hobbies": "game, running",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "c, java",
        "job": "devops"
    },

 {
    "name": "Bui Dac Cong",
        "email": "ghi@gmail.com",
        "birthday": "2002-11-14",
        "characteristic": "carefree, lazy, jealous",
        "hobbies": "running, book",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese, Korean, English",
        "p_lang": "python, golang",
        "job": "ai-data"
    },

    {        "name": "Tao Dac Minh",
        "email": "mno@gmail.com",
        "birthday": "1992-09-30",
        "characteristic": "jealous, hardworking",
        "hobbies": "book",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "java, c",
        "job": "fullstack"
    },

    {
    "name": "Vu Sy Cuong",
        "email": "jkl@gmail.com",
        "birthday": "1992-11-05",
        "characteristic": "selfish",
        "hobbies": "badminton, game",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "sql, python, javascript",
        "job": "devops"
    },

    {
    "name": "Dao Dac Hieu",
        "email": "pqr@gmail.com",
        "birthday": "1999-07-29",
        "characteristic": "selfish",
        "hobbies": "running, badminton",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese, Chinese, English",
        "p_lang": "rust, golang",
        "job": "devops"
    },

    {
    "name": "Ha Dac Viet",
        "email": "ghi@gmail.com",
        "birthday": "2003-12-08",
        "characteristic": "creative, considerate, lazy",
        "hobbies": "baseball, coding",
        "addInf": "",
        "loc": "Da Nang, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "rust",
        "job": "student"
    },

    {
    "name": "Tao Trong Vu",
        "email": "ghi@gmail.com",
        "birthday": "1991-02-01",
        "characteristic": "quite, jealous, hardworking",
        "hobbies": "book, running, baseball",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "rust, javascript, golang",
        "job": "ai-data"
    },

    {
    "name": "Tran Thanh Hieu",
        "email": "abc@gmail.com",
        "birthday": "1995-04-10",
        "characteristic": "humor, considerate, lazy",
        "hobbies": "coding, game",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "rust",
        "job": "ios"
    },

    {
    "name": "Vo Trong Minh",
        "email": "abc@gmail.com",
        "birthday": "1997-01-04",
        "characteristic": "jealous",
        "hobbies": "running, badminton",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "java",
        "job": "student"
    },

    {
    "name": "Bui Dac Kien",
        "email": "ghi@gmail.com",
        "birthday": "2002-11-21",
        "characteristic": "rude",
        "hobbies": "coding, running",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "java",
        "job": "front-end"
    },

    {
    "name": "Tao Kim Thanh Viet",
        "email": "ghi@gmail.com",
        "birthday": "2004-02-02",
        "characteristic": "intelligent, humor, carefree",
        "hobbies": "running, game, badminton",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "c++, golang, java",
        "job": "game"
    },

    {
    "name": "Trinh Phuong Minh Nam",
        "email": "mno@gmail.com",
        "birthday": "2001-09-06",
        "characteristic": "creative, rude",
        "hobbies": "badminton",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, Korean, English",
        "p_lang": "golang, c, java",
        "job": "fullstack"
    },

    {
    "name": "Pham Cong Cuong",
        "email": "def@gmail.com",
        "birthday": "1994-05-09",
        "characteristic": "carefree",
        "hobbies": "coding, book, badminton",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "python, sql, c",
        "job": "ios"
    },

    {
    "name": "Vo Trong Anh",
        "email": "abc@gmail.com",
        "birthday": "1993-09-12",
        "characteristic": "quite, considerate",
        "hobbies": "book, running",
        "addInf": "",
        "loc": "Ho Chi Minh, Vietnam",
        "lang": "Vietnamese, Korean, Chinese",
        "p_lang": "java",
        "job": "android"
    },

    {
    "name": "Tran Cong Cong",
        "email": "mno@gmail.com",
        "birthday": "1993-09-16",
        "characteristic": "considerate, jealous",
        "hobbies": "running, book",
        "addInf": "",
        "loc": "Binh Duong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "golang",
        "job": "game"
    },

    {
    "name": "Bui Trong Cong",
        "email": "def@gmail.com",
        "birthday": "1996-08-11",
        "characteristic": "jealous, intelligent, selfish",
        "hobbies": "game, running",
        "addInf": "",
        "loc": "Hai Phong, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "javascript, python",
        "job": "ai-data"
    },

    {
    "name": "Pham Thanh Long",
        "email": "abc@gmail.com",
        "birthday": "1990-04-23",
        "characteristic": "shy",
        "hobbies": "book",
        "addInf": "",
        "loc": "Can Tho, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "rust",
        "job": "back-end"
    },

    {
    "name": "Nguyen Minh Khiem",
        "email": "ghi@gmail.com",
        "birthday": "2005-11-02",
        "characteristic": "hardworking",
        "hobbies": "running, baseball",
        "addInf": "",
        "loc": "Ha Noi, Vietnam",
        "lang": "Vietnamese, English, Korean",
        "p_lang": "c, golang, javascript",
        "job": "devops"
    },

    {
    "name": "Tran Song Cuong",
        "email": "mno@gmail.com",
        "birthday": "2000-06-04",
        "characteristic": "creative, humor, considerate",
        "hobbies": "game",
        "addInf": "",
        "loc": "Dak Lak, Vietnam",
        "lang": "Vietnamese",
        "p_lang": "java, javascript, rust",
        "job": "cyber"
    }

]


# Convert mentor data into DataFrame
mentors_df = pd.DataFrame(mentors_data)


# Concatenate mentor features for TF-IDF vectorization
mentors_df['features'] = mentors_df['characteristic'].replace(", ", " ") + ' ' + mentors_df['hobbies'].replace(", ", " ") + ' ' + \
                          mentors_df['loc'].replace(", ", " ") + ' ' + mentors_df['lang'].replace(", ", " ") + ' ' + \
                          mentors_df['p_lang'].replace(", ", " ") + ' ' + mentors_df['job'].replace(", ", " ")

# TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(mentors_df['features'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend_mentors(name, location=None, language=None, programming_language=None, job=None):
    # Find index of the mentor with given name
    mentor_index = mentors_df[mentors_df['name'] == name].index[0]
    
    # Filter mentors based on user-specified criteria
    filtered_mentors_df = mentors_df.copy()
    if (location!=""):
        filtered_mentors_df = filtered_mentors_df[filtered_mentors_df['loc'] == location]
    if (language!=""):
        filtered_mentors_df = filtered_mentors_df[filtered_mentors_df['lang'] == language]
    if (programming_language!=""):
        filtered_mentors_df = filtered_mentors_df[filtered_mentors_df['p_lang'] == programming_language]
    if (job!="any"):
        filtered_mentors_df = filtered_mentors_df[filtered_mentors_df['job'] == job]
    
    # Compute similarity scores for filtered mentors
    tfidf_matrix_filtered = tfidf_vectorizer.transform(filtered_mentors_df['features'])
    mentor_similarities = cosine_similarity(tfidf_matrix_filtered, tfidf_matrix_filtered)
    
    # Get similarity scores for the mentor
    mentor_sim_scores = list(enumerate(mentor_similarities[mentor_index]))
    
    # Sort mentors by similarity scores
    mentor_sim_scores = sorted(mentor_sim_scores, key=lambda x: x[1], reverse=True)
    
    # Exclude the mentor itself
    mentor_sim_scores = mentor_sim_scores[1:]
    
    # Get top 3 similar mentors
    top_mentors_indices = [i[0] for i in mentor_sim_scores[:3]]

    # Return recommended mentors
    recommended_mentors = filtered_mentors_df.iloc[top_mentors_indices]['name']
    return recommended_mentors.tolist()

# Example usage:
# Replace 'John Doe' with the name of the mentor you want to find recommendations for
# You can also provide additional filter parameters such as location, hobbies, language, programming language, and job
recommended_mentors = recommend_mentors(user_name, loc, lang, plang, job)
print(recommended_mentors)
