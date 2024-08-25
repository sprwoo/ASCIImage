import React from "react";
import { useState } from "react";

const App = () => {
    const [userImage, setImage] = useState(null);
    const [ascii, setASCII] = useState(null);
    
    const handleImage = (e) => {
        const file = e.target.files[0];
        if (file) {
            setImage(file);
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const img = new FormData();
        img.append("image", userImage);

        try {
            const response = await fetch("https://asci-image-pythonscript.vercel.app/upload", {
                method: "POST",
                body: img,
            });

            const ASCIIText = await response.json();
            console.log(ASCIIText.ascii_text);
            setASCII(ASCIIText.ascii_text);
        } catch (error) {
            console.error("Error uploading file", error);
        }
    };

    return (
        <div class="main-container">
            <h1>ASCIImage</h1>
            <div id="imageUpload">
                <form onSubmit={handleSubmit}>
                    <input type="file" name="image" onChange={handleImage} />
                    <button type="submit">Upload and Extract Text</button>
                </form>

                {ascii && (
                <div>
                    <h3>Extracted Text:</h3>
                    <p dangerouslySetInnerHTML={{ __html: ascii }}></p>
                </div>
                )}
            </div>
        </div>
    )
}

export default App;
