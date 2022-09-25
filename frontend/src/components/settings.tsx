import { Dispatch, SetStateAction } from 'react';

import { borderSizes, aspectRatios } from '@common/static';
import { EqualBorderToggle } from '@components/equal-border-toggle';
import { Radio } from '@components/radio';

interface Props {
    evenBorder: boolean;
    setEvenBorder: Dispatch<SetStateAction<boolean>>;
    borderWidth: string;
    setBorderWidth: Dispatch<SetStateAction<string>>;
    aspectRatio: string;
    setAspectRatio: Dispatch<SetStateAction<string>>;
}

export const Settings = ({
    evenBorder,
    setEvenBorder,
    borderWidth,
    setBorderWidth,
    aspectRatio,
    setAspectRatio,
}: Props) => {
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
