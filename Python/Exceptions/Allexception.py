
def do_something(thing):
    x =0
    y =1
    try:
        y=2
        print("Hello :"+ thing)
        print(x)

    except ZeroDivisionError:
        print(x,"is zero")
    except Exception as e:
        print(e)

    else:
        print(x)

    finally:
        print("the end of project")


do_something(4)
print("___________")
do_something("shalom")