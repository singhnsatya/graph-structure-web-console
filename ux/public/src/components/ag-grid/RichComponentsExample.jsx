import React, {Component} from "react";

import {AgGridReact} from "ag-grid-react";
import RatioRenderer from "./RatioRenderer.jsx";
import ClickableRenderer from "./ClickableRenderer.jsx";

export default class RichComponentsExample extends Component {
    constructor(props) {
        super(props);

        this.state = {
            rowData: RichComponentsExample.createRowData(),
            columnDefs: RichComponentsExample.createColumnDefs()
        };

        this.onGridReady = this.onGridReady.bind(this);
    }

    onGridReady(params) {
        this.gridApi = params.api;
        this.columnApi = params.columnApi;

        this.gridApi.sizeColumnsToFit();
    }

    /*static createColumnDefs() {
        return [
            {
                headerName: "Name",
                field: "name",
                width: 200
            },
            {
                headerName: "Ratio Component",
                field: "ratios",
                cellRendererFramework: RatioRenderer,
                width: 350
            },
            {
                headerName: "Clickable Component",
                field: "name",
                cellRendererFramework: ClickableRenderer,
                width: 250
            }
        ];    }*/

    static createColumnDefs() {
        return [
            {
                headerName: "Empid",
                field: "empid",
                width: 200
            },
            {
                headerName: "Name",
                field: "name",
                width: 350
            },
            {
                headerName: "Age",
                field: "age",
                width: 200
            },
            {
                headerName: "Joining",
                field: "joining",
                width: 200
            },
            {
                headerName: "Address",
                field: "address",
                width: 200
            },
            {
                headerName: "Parent",
                field: "parent",
                width: 200
            }
        ];    
    }

    static createRowData() {
        return [
            {empid: 1, name: 'Homer Simpson', age: 25, joining: "2012-10-12", address: "Mumbai", parent: 0},
            {empid: 2, name: 'josh', age: 35, joining: "2003-07-15", address: "mumbai", parent: 1},
            {empid: 3, name: 'akash', age: 32, joining: "2006-06-20", address: "surat", parent: 2},
            {empid: 4, name: 'sagar', age: 31, joining: "2009-06-20", address: "bangalore", parent: 3},
            {empid: 5, name: 'akashay', age:29, joining: "2010-02-02", address: "gujarat", parent: 4}
        ];
    }

    render() {
        return (
            <div style={{height: 370, width: 900}} className="ag-fresh">
                <AgGridReact
                    // properties
                    columnDefs={this.state.columnDefs}
                    rowData={this.state.rowData}
                    gridOptions={this.state.gridOptions}

                    // events
                    onGridReady={this.onGridReady}>
                </AgGridReact>
            </div>
        );
    }
};