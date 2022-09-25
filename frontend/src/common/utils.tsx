export const createImage = async (
    formData: FormData
): Promise<[string | undefined, undefined | unknown]> => {
    try {
        const res = await fetch('http://localhost:8000/images/generate', {
            method: 'POST',
            body: formData,
        });
        if (res.status != 200) {
            throw new Error('something went wrong!');
        }
        const blob = await res.blob();
        return [URL.createObjectURL(blob), undefined];
    } catch (err) {
        return [undefined, err];
    }
};
