"""
Filename:  main.py
Title: QR Code generator
Author: Raghava | GitHub: @raghavtwenty
Date Created: May 12, 2024 | Last Updated: May 12, 2024
Language: Python | Version: 3.10.13, 64-bit
"""

# Importing required libraries
import streamlit as st
import qrcode
from io import BytesIO


# Generate QR Code
def generate_qr_code(data, color="black", background="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=color,
        back_color=background,
    )
    return img


def main():
    st.title("QR Code Generator")

    # Input text
    input_text = st.text_input("Enter text / link")

    # Customizable options
    color = st.color_picker("Choose color for QR code", "#000000")
    background_color = st.color_picker("Choose background color", "#FFFFFF")

    # Final show
    if st.button("Generate"):
        qr_img = generate_qr_code(input_text, color, background_color)
        img_byte_array = BytesIO()
        qr_img.save(img_byte_array, format="PNG")
        st.image(img_byte_array, caption="Generated QR Code", use_column_width=True)

    # Footer
    st.markdown(
        """---\n
Designed & Developed by Raghava \n
GitHub: [@raghavtwenty](https://github.com/raghavtwenty) \n
Date Created: May 12, 2024 · Last Updated: May 12, 2024 · Version Info: 1.12052024\n
"""
    )


# Main
if __name__ == "__main__":
    st.set_page_config(page_title="QR Code Generator")
    main()
