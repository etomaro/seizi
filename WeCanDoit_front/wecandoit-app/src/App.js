import React from "react";

import { Routes, Route } from "react-router-dom";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Container from "@mui/material/Container";

import Header from "./components/Layout/Header";
import Footer from "./components/Layout/Footer";

import Dashboard from "./components/dashborad/Dashboard";
import Twitter from "./Twitter/Twitter";
import ChartJsTest1 from "./components/ChartJsTest1";

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export function App() {
    return (
        <>
            <ThemeProvider theme={defaultTheme}>
                <Box sx={{ display: "flex" }}>
                    <Header />;
                    <Box
                        component="main"
                        sx={{
                            backgroundColor: (theme) =>
                                theme.palette.mode === "light"
                                    ? theme.palette.grey[100]
                                    : theme.palette.grey[900],
                            flexGrow: 1,
                            height: "100vh",
                            overflow: "auto",
                        }}
                    >
                        <Toolbar />
                        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
                            <Routes>
                                <Route path="/" element={<Dashboard />} />
                                <Route path="/twitter" element={<Twitter />} />
                                <Route
                                    path="/chartjs"
                                    element={<ChartJsTest1 />}
                                />
                            </Routes>
                            <Footer sx={{ pt: 4 }} />
                        </Container>
                    </Box>
                </Box>
            </ThemeProvider>
        </>
    );
}

export default App;
