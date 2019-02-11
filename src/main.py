import module_import
from examples import data_types
from examples.oop import class_example

x = 50

# In Python there's no main script to run.
# __name__ is a built in variable. It gets assigned a string depending on how you're running the script.
# If you run it directly, then it gets the string __main__
if __name__ == "__main__":
    data_types.data_types_examples()
    class_example.class_example()

    def reassign_global():
        global x
        x = 200


    reassign_global()
    print(x)

    module_import.module_import_example()

