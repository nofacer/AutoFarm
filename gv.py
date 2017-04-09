file_object = open('data.txt')
try:
    all_the_text = file_object.read( )
except:
    file_object_2 = open('default.txt')
    all_the_text = file_object_2.read( )
    file_object_2.close( )


finally:
     file_object.close( )


warn_line=int(all_the_text)

