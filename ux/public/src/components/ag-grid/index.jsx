import React from "react"
import {render} from "react-dom"
import store from '../../store/EmployeeStore.js'
import Grid from './RichComponentsExample.jsx'
import { Provider  } from 'mobx-react';

render(
	 <Provider store = {store}>
    <Grid />
    </Provider>,
    document.querySelector('#root')
);