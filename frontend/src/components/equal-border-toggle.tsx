import { Dispatch, SetStateAction } from 'react';

interface Props {
    isToggled: boolean;
    handleChange: Dispatch<SetStateAction<boolean>>;
}

export const EqualBorderToggle = ({ isToggled, handleChange }: Props) => {
    const onChange = () => {
        handleChange(!isToggled);
    };

    return (
        <div className="flex content-center gap-4">
            <input
                type="checkbox"
                checked={isToggled}
                onChange={onChange}
                className="checkbox checkbox-secondary self-center"
            />
            <span>Equal borders</span>
        </div>
    );
};
