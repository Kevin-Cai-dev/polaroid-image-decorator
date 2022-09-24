import { InputSettings } from '@common/types';
import { GithubCorner } from '@components/github-corner';
import { Settings } from '@components/settings';
import type { NextPage } from 'next';
import { useState, useRef, ChangeEvent } from 'react';

const Home: NextPage = () => {
    const [selectedFile, setSelectedFile] = useState<File>();
    const [inputSettings, setInputSettings] = useState<InputSettings>();
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
        console.log(selectedFile);
        console.log(inputSettings);
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
            <div className="flex flex-col gap-8">
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
