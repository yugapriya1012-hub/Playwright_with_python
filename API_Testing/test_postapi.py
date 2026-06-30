# from playwright.sync_api import sync_playwright

# def test_create_user():
#     with sync_playwright() as p:
#         request=p.request.new_context()

#         response=request.post(
#             "https://jsonplaceholder.typicode.com/users",
#             data={
#                 "name":"Name_1",
#                 "job":"QA Engineer"
#             }
#         )

#         assert response.status in [200,201]

#         body=response.json()
#         print(body)

#         assert body["name"]=="Name_1"
