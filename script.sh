### POST

curl --location --request POST 'http://127.0.0.1:8000/bookmark' \
--header 'Username: test' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw '{
    "title": "test",
    "url": "http://www.somelink.com/to/my.pdf",
    "isPublic": false
}'


curl --location --request POST 'http://127.0.0.1:8000/bookmark' \
--header 'Username: test2' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw '{
    "title": "test2",
    "url": "http://www.somelink.com/to/my.pdf",
    "isPublic": false
}'

curl --location --request POST 'http://127.0.0.1:8000/bookmark' \
--header 'Username: test2' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw '{
    "title": "test2.2",
    "url": "http://www.somelink.com/to/my.pdf",
    "isPublic": true
}'

### GET

curl --location --request GET 'http://127.0.0.1:8000/bookmarks' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request GET 'http://127.0.0.1:8000/bookmarks' \
--header 'Username: test' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request GET 'http://127.0.0.1:8000/bookmarks' \
--header 'Username: test' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request GET 'http://127.0.0.1:8000/bookmarks' \
--header 'Username: test2' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request GET 'http://127.0.0.1:8000/bookmark/1' \
--header 'Username: test' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request GET 'http://127.0.0.1:8000/bookmark/2' \
--header 'Username: test' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request GET 'http://127.0.0.1:8000/bookmark/3' \
--header 'Username: test' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

### PATCH

curl --location --request PATCH 'http://127.0.0.1:8000/bookmark/2' \
--header 'Username: test' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request PATCH 'http://127.0.0.1:8000/bookmark/2' \
--header 'Username: test' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request PATCH 'http://127.0.0.1:8000/bookmark/1' \
--header 'Username: test' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw '{
    "title": "not2",
    "url": "http://11.com",
    "isPublic": true
}'

### DELETE

curl --location --request DELETE 'http://127.0.0.1:8000/bookmark/1' \
--header 'Username: test2' \
--header 'Authorization: Bearer 3563cfb3-df7c-43b5-85b3-7509ba59bd22' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request DELETE 'http://127.0.0.1:8000/bookmark/1' \
--header 'Username: test2' \
--header 'Authorization: Bearer 3563cfb3-df7c-43b5-85b3-7509ba59bd22' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''

curl --location --request DELETE 'http://127.0.0.1:8000/bookmark/2' \
--header 'Username: test2' \
--header 'Authorization: Bearer 3563cfb3-df7c-43b5-85b3-7509ba59bd22' \
--header 'Cookie: csrftoken=If2G1YvvnkiCOSZ2vRYl5i0Bvs1Mr46s38UtS0DxVtC2OuolXhORLLQVNObybtUc; sessionid=4a7ec1vw0ghltb4tq5zzjkfv5xb7y924' \
--data-raw ''