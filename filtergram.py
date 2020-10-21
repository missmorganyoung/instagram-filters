import filters

def main():
    im = filters.load_img("hdcitylights.jpg")
    filtered_im = filters.grayscale(im)
    filters.show_img(filtered_im)

if __name__ == "__main__":
    main()
