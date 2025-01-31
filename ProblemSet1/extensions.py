user_input = input("File Name: ")
user_inputs = user_input.strip().lower()
if user_inputs.endswith(".gif"):
    print("image/gif")
elif user_inputs.endswith("jpg"):
    print("image/jpeg")
elif user_inputs.endswith(".png"):
    print("image/png")
elif user_inputs.endswith(".jpeg"):
    print("image/jpeg")
elif user_inputs.endswith(".pdf"):
    print("application/pdf")
elif user_inputs.endswith(".txt.pdf"):
    print("doc/pdf")
elif user_inputs.endswith(".txt"):
    print("text/plain")
elif user_inputs.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
