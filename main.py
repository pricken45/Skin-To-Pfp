from PIL import Image, ImageDraw, ImageFilter

def defining():
    global im1, eraser, im3

    im1 = Image.open('skin.png').convert("RGBA")
    eraser = Image.open('eraser.png')
    im3 = Image.open('final.png').convert("RGBA")
    #shadows = Image.open("")

def cropping():
    global head, head2, body1, body2, arm1, arm2

    # Crop out all of the body-parts
    head = im1.crop((5,9,15,16))
    head2 = im1.crop((37, 8, 47, 15))

    body1 = im1.crop((21,20,27,21))
    body2 = im1.crop((20,21,28,32))

    arm1 = im1.crop((47,20,50,32))
    arm2 = im1.crop((41, 52, 42, 64))

    
def pasting():
    im3.paste(eraser,(0,0)) # Erase first so it doesnt overlap
    im3.paste(head, (5, 4)) # Paste head
    im3.paste(head2, (5, 4))
    im3.paste(body1,(7,11)) # Paste shoulders
    im3.paste(body2,(6,12)) # Paste body
    

# Call all the functions
defining()
cropping()
pasting()

# Save the final product
im3.save("final.png")
