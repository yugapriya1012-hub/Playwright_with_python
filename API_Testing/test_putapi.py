# from playwright.sync_api import sync_playwright

# def test_update_user():
#     with sync_playwright() as p:
#         request=p.request.new_context()

#         response=request.put(
#             "https://jsonplaceholder.typicode.com/users/1",
#             data={
#                 "name":"Name_2",
#                 "job":"Senior QA"
#             }
#         )

#         assert response.status==200