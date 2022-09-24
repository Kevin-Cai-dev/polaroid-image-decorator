import { borderSizes, aspectRatios } from '@common/static';
import { InputSettings } from '@common/types';
import { EqualBorderToggle } from '@components/equal-border-toggle';
import { Radio } from '@components/radio';
import { useState, useEffect, Dispatch, SetStateAction } from 'react';

interface Props {
    handleUpdate: Dispatch<SetStateAction<InputSettings>>;
}

export const Settings = ({ handleUpdate }: Props) => {
    const [evenBorder, setEvenBorder] = useState(false);
    const [borderWidth, setBorderWidth] = useState('md_borders');
    const [aspectRatio, setAspectRatio] = useState('ratio_1_1');

    useEffect(() => {
        handleUpdate({
            evenBorder,
            borderWidth,
            aspectRatio,
        });
        console.log('updated');
    }, [handleUpdate, evenBorder, borderWidth, aspectRatio]);

    return (
        <>
            <h2 className="mt-4 mb-0">Settings</h2>
            <EqualBorderToggle
                isToggled={evenBorder}
                handleChange={setEvenBorder}
            />
            <div className="flex flex-wrap gap-6">
                {borderSizes.map((data) => (
                    <Radio
                        data={data}
                        currentValue={borderWidth}
                        handleChange={setBorderWidth}
                        key={data.value}
                    />
                ))}
            </div>
            <div className="flex flex-wrap gap-6">
                {aspectRatios.map((data) => (
                    <Radio
                        data={data}
                        currentValue={aspectRatio}
                        handleChange={setAspectRatio}
                        key={data.value}
                        disabled={evenBorder}
                    />
                ))}
            </div>
        </>
    );
};
