import * as React from "react";
import { useTheme } from "@mui/material/styles";
import {
    BarChart,
    Bar,
    Cell,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer,
} from "recharts";
import { datas } from "./Datas";
import { Typography } from "@mui/material";

const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
        return (
            <div className="custom-tooltip">
                <p className="label">{`${label} : ${payload[0].value}`}</p>
                {/* <p className="intro">{{ datas }}</p> */}
                <p className="desc">{`${label} : ${payload}`}</p>
            </div>
        );
    }

    return null;
};

const BarGraph = () => {
    return (
        <>
            <Typography
                component="h2"
                variant="h6"
                color="secondary"
                gutterBottom
            >
                followerRank
            </Typography>
            <ResponsiveContainer>
                <BarChart
                    width={500}
                    height={300}
                    // layout="vertical"
                    data={datas}
                    margin={{
                        top: 5,
                        right: 30,
                        left: 20,
                        bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="id" />
                    <YAxis />
                    {/* <Tooltip content={<CustomTooltip />} /> */}
                    <Tooltip />
                    <Legend />
                    <Bar dataKey="follower" fill="#8884d8" />
                    <Bar dataKey="follow" fill="#82ca9d" />
                    <Bar dataKey="name" fill="#" />
                </BarChart>
            </ResponsiveContainer>
        </>
    );
};

export default BarGraph;
