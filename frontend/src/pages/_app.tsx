import { ThemeProvider } from 'next-themes';
import type { AppProps } from 'next/app';
import Head from 'next/head';

import '../styles/globals.css';

function MyApp({ Component, pageProps }: AppProps) {
    return (
        <ThemeProvider defaultTheme="dracula">
            <Head>
                <title>Polaroid Image Decorator</title>
            </Head>
            <Component {...pageProps} />
        </ThemeProvider>
    );
}

export default MyApp;
