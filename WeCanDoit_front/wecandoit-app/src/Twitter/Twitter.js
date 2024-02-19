import React from "react";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";

import BarGraph from "./BarGraph";
import Value from "./Value";
import TwitterTable from "./TwitterTable";

const Twitter = () => {
    return (
        <>
            <Grid container spacing={3}>
                {/* Chart */}
                <Grid item xs={12} md={8} lg={9}>
                    <Paper //コンテンツが紙に乗っているような感じ
                        sx={{
                            p: 2,
                            display: "flex",
                            flexDirection: "column",
                            height: 440,
                        }}
                    >
                        <BarGraph />
                    </Paper>
                </Grid>
                {/* 平均値 */}
                <Grid item xs={12} md={4} lg={3}>
                    <Paper
                        sx={{
                            p: 2,
                            display: "flex",
                            flexDirection: "column",
                            height: 240,
                        }}
                    >
                        <Value />
                    </Paper>
                </Grid>
                {/* Recent Orders */}
                <Grid item xs={12}>
                    <Paper
                        sx={{
                            p: 2,
                            display: "flex",
                            flexDirection: "column",
                        }}
                    >
                        <TwitterTable />
                    </Paper>
                </Grid>
            </Grid>
        </>
    );
};

export default Twitter;
