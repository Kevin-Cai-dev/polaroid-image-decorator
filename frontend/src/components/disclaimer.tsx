import { ReactNode } from 'react';

interface Props {
    children: ReactNode;
}

const DisclaimerMessage = ({ children }: Props) => {
    return <p className="m-0">{children}</p>;
};

export const Disclaimer = () => {
    const message = (
        <DisclaimerMessage>
            {
                "✨ If you run into a fetch error, most likely the backend isn't running ¯\\_(ツ)_/¯"
            }
        </DisclaimerMessage>
    );
    const returnFormat = (
        <DisclaimerMessage>
            Note that images are returned in <code>JPEG</code> format
        </DisclaimerMessage>
    );

    return (
        <div className="mb-4 border-l-4 border-accent pl-4 italic">
            {message}
            {returnFormat}
        </div>
    );
};
