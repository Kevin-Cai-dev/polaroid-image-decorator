export const createImage = async (
    formData: FormData
): Promise<[string | undefined, string | undefined]> => {
    try {
        const res = await fetch(
            `${process.env.NEXT_PUBLIC_API_ENDPOINT}/images/generate`,
            {
                method: 'POST',
                body: formData,
            }
        );
        if (res.status != 200) {
            const errorBody = await res.json();
            throw new Error(errorBody.detail);
        }
        const blob = await res.blob();
        return [URL.createObjectURL(blob), undefined];
    } catch (err) {
        if (err instanceof Error) {
            return [undefined, err.message];
        }
        return [
            undefined,
            'something went wrong while trying to create the new image',
        ];
    }
};
