import os

print("当前目录：", os.getcwd())
print("当前目录里有什么：", os.listdir())
os.makedirs("project", exist_ok=True)
print(os.path.exists("project"))
print("目录展示完毕")
