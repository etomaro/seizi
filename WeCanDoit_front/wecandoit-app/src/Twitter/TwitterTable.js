import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import { datas } from "./Datas";
import { TableContainer, TablePagination, Typography } from "@mui/material";

const TwitterTable = () => {
    const [page, setPage] = React.useState(0);
    const [rowsPerPage, setRowsPerPage] = React.useState(10);

    const handleChangePage = (event, newPage) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(+event.target.value);
        setPage(0);
    };

    return (
        <>
            <Typography
                component="h2"
                variant="h6"
                color="secondary"
                gutterBottom
            >
                Table
            </Typography>
            <TableContainer sx={{ maxHeight: 220, maxWidth: 1200 }}>
                <Table size="small" stickyHeader aria-label="sticky table">
                    <TableHead>
                        <TableRow>
                            <TableCell>id</TableCell>
                            <TableCell>name</TableCell>
                            <TableCell>prefecture</TableCell>
                            <TableCell>twitter_id</TableCell>
                            <TableCell>follower</TableCell>
                            <TableCell>follow</TableCell>
                            <TableCell align="right">district</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {datas
                            .slice(
                                page * rowsPerPage,
                                page * rowsPerPage + rowsPerPage
                            )
                            .map((data) => (
                                <TableRow
                                    key={data.id}
                                    hover
                                    role="checkbox"
                                    tabIndex={-1}
                                >
                                    <TableCell>{data.id}</TableCell>
                                    <TableCell>{data.name}</TableCell>
                                    <TableCell>{data.prefecture}</TableCell>
                                    <TableCell>{data.twitter_id}</TableCell>
                                    <TableCell>{data.follower}</TableCell>
                                    <TableCell>{data.follow}</TableCell>
                                    <TableCell align="right">
                                        {data.district}
                                    </TableCell>
                                </TableRow>
                            ))}
                    </TableBody>
                </Table>
            </TableContainer>
            <TablePagination
                rowsPerPageOptions={[10, 25, 100]}
                component="div"
                count={datas.length}
                rowsPerPage={rowsPerPage}
                page={page}
                onPageChange={handleChangePage}
                onRowsPerPageChange={handleChangeRowsPerPage}
            />
        </>
    );
};

export default TwitterTable;
