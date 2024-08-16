import React from "react";
import { useState } from "react";

const App = () => {
    const [selectedImage, setSelectedImage] = useState(null);
    
    const handleImage = (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setSelectedImage(reader.result);
            }
            reader.readAsDataURL(file);
        }
    }


    
    return (
        <div id="imageUpload">
            <input
                type="file"
                accept="image/*"
                onChange={handleImage}
            />
            {selectedImage && (
                <div>
                    <img src={selectedImage} alt="Selected" style={{ width: '300px', height: 'auto' }} />
                </div>
            )}
        </div>
    )
}

export default App;
