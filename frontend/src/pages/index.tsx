import type { NextPage } from 'next';
import { useState, useRef, ChangeEvent } from 'react';

import { InputSettings } from '@common/types';
import { GithubCorner } from '@components/github-corner';
import { Settings } from '@components/settings';

const Home: NextPage = () => {
    const [selectedFile, setSelectedFile] = useState<File>();
    const [inputSettings, setInputSettings] = useState<InputSettings>({
        evenBorder: false,
        borderWidth: '',
        aspectRatio: '',
    });
    const hiddenFileInput = useRef<HTMLInputElement>(null);

    const onFileClick = () => {
        hiddenFileInput.current?.click();
    };

    const handleUpload = (e: ChangeEvent<HTMLInputElement>) => {
        e.target.files && setSelectedFile(e.target.files[0]);
    };

    const createImage = () => {
        /**
         * TODO
         * - Send a POST request with both file and inputSettings in the body
         * - receive new image from backend and render
         */
        const formData = new FormData();
        selectedFile && formData.append('file', selectedFile);
        formData.append('params', JSON.stringify(inputSettings));
        console.log(formData.get('file'));
        fetch('http://localhost:8000/images/generate', {
            method: 'POST',
            body: formData,
        })
            .then((res) => res.json())
            .then((data) => console.log(data))
            .catch((err) => console.log(err));
    };

    return (
        <div className="prose mx-auto max-w-screen-lg p-8">
            <GithubCorner />
            <h1 className="text-center font-sans font-bold">
                Polaroid Image Generator
            </h1>
            <input
                type="file"
                name="file"
                id="file-upload"
                accept=".jpg, .jpeg, .png"
                ref={hiddenFileInput}
                className="hidden"
                onChange={handleUpload}
            />
            <button className="btn btn-primary" onClick={onFileClick}>
                Upload image
            </button>
            <span className="pl-4">
                {selectedFile ? selectedFile.name : 'No file chosen'}
            </span>
            <div className="divider" />
            <div className="flex flex-col gap-10">
                <Settings handleUpdate={setInputSettings} />
                <button
                    className="btn btn-accent"
                    onClick={createImage}
                    disabled={!selectedFile}
                >
                    Generate!
                </button>
            </div>
        </div>
    );
};

export default Home;
