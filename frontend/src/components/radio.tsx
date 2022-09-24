import { Dispatch, SetStateAction } from 'react';

interface Props {
    data: {
        display: string;
        value: string;
        group: string;
    };
    currentValue: string;
    handleChange: Dispatch<SetStateAction<string>>;
    disabled?: boolean;
}

export const Radio = ({
    data,
    currentValue,
    handleChange,
    disabled = false,
}: Props) => {
    return (
        <span className="flex content-center gap-4">
            <input
                type="radio"
                name={data.group}
                className="radio radio-secondary self-center"
                disabled={disabled}
                onChange={() => handleChange(data.value)}
                checked={currentValue === data.value}
            />
            <span>{data.display}</span>
        </span>
    );
};
