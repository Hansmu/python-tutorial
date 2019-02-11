def catch_error(number):
    try:
        result = 10 + number
    except TypeError:
        print('Error happened')
    except EOFError:
        print('End of file')
    except:
        print('Default run')
    else:  # Else goes together with the except blocks. If no errors are thrown, then it gets run.
        print('No errors.')
    finally:
        print('Finished execution.')
