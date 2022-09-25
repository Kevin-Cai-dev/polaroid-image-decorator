import type { NextPage } from 'next';
import { useState, useRef, ChangeEvent } from 'react';

import { createImage } from '@common/utils';
import { ErrorAlert } from '@components/error-alert';
import { GithubCorner } from '@components/github-corner';
import { Settings } from '@components/settings';

const Home: NextPage = () => {
    const [selectedFile, setSelectedFile] = useState<File>();
    const [newImage, setNewImage] = useState<string>();
    const [evenBorder, setEvenBorder] = useState(false);
    const [borderWidth, setBorderWidth] = useState('md_borders');
    const [aspectRatio, setAspectRatio] = useState('ratio_1_1');
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const hiddenFileInput = useRef<HTMLInputElement>(null);

    const settingsProps = {
        evenBorder,
        setEvenBorder,
        borderWidth,
        setBorderWidth,
        aspectRatio,
        setAspectRatio,
    };

    const onFileClick = () => {
        hiddenFileInput.current?.click();
    };

    const handleUpload = (e: ChangeEvent<HTMLInputElement>) => {
        e.target.files && setSelectedFile(e.target.files[0]);
    };

    const getImage = async () => {
        const formData = new FormData();
        selectedFile && formData.append('file', selectedFile);
        formData.append('even_border', evenBorder.toString());
        formData.append('border_width_key', borderWidth);
        formData.append('aspect_ratio_key', aspectRatio);

        setNewImage(undefined);
        setIsError(false);
        setIsLoading(true);
        const [response, error] = await createImage(formData);
        setIsLoading(false);
        if (error) {
            return setIsError(true);
        }
        setNewImage(response);
    };

    return (
        <div className="prose mx-auto min-h-screen max-w-screen-lg p-8">
            <GithubCorner />
            <h1 className="text-center font-sans font-bold">
                Polaroid Image Generator
            </h1>
            <input
                type="file"
                name="image-upload"
                accept=".jpg, .jpeg, .png, .tiff, .webp"
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
                <Settings {...settingsProps} />
                <button
                    className="btn btn-secondary"
                    onClick={getImage}
                    disabled={!selectedFile}
                >
                    Generate!
                </button>
            </div>
            <div className="divider" />
            {isLoading && <progress className="progress progress-primary" />}
            {isError && <ErrorAlert />}
            {newImage && !isLoading && (
                <>
                    <a
                        href={newImage}
                        download={`POLAROID_${selectedFile?.name}`}
                        className="btn btn-accent"
                    >
                        Download image
                    </a>
                    <picture>
                        <source srcSet={newImage} type="image/jpeg" />
                        <img src={newImage} alt="" />
                    </picture>
                </>
            )}
        </div>
    );
};

export default Home;
