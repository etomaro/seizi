import React, { useEffect, useState } from "react";
import { datas } from "./Datas";
import { Typography } from "@mui/material";

const Value = () => {
    const [aveFollower, setAveFollower] = useState();
    const [maxFollower, setMaxFollower] = useState();
    useEffect(() => {
        const follower = datas.map((data) => data.follower);
        setAveFollower(
            Math.round(follower.reduce((a, b) => a + b) / follower.length)
        );
        setMaxFollower(follower.reduce((a, b) => Math.max(a, b)));
    }, []);

    return (
        <>
            <Typography
                component="h2"
                variant="h6"
                color="secondary"
                gutterBottom
            >
                follower平均値
            </Typography>
            <Typography component="p" variant="h4">
                {aveFollower} 人
            </Typography>
            <Typography
                component="h2"
                variant="h6"
                color="secondary"
                gutterBottom
                sx={{ mt: 3 }}
            >
                follower最大値
            </Typography>
            <Typography component="p" variant="h4">
                {maxFollower} 人
            </Typography>
        </>
    );
};

export default Value;
