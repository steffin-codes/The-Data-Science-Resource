from .classmodule import MyClass

def main():
    my_object = MyClass()
    my_object.get_project_details()
    my_object.gen_project_meta_files()
    print("All done!")

if __name__ == '__main__':
    main()