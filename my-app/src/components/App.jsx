import React from "react";
import { useState } from "react";

const App = () => {
    const [image, setImage] = useState(null);
    
    const handleImage = (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setImage(reader.result);
            }
            reader.readAsDataURL(file);
        }
    }


    return (
        <div class="main-container">
            <h1>ASCIImage</h1>
            <div id="imageUpload">
                <input
                    type="file"
                    accept="image/*"
                    onChange={handleImage}
                />
                {image && (
                    <div>
                        <img src={image} alt="Selected" style={{ width: '300px', height: 'auto' }} />
                    </div>
                )}
            </div>
        </div>
    )
}

export default App;
