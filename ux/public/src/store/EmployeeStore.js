import { autorun, computed, observable, action } from 'mobx';

var data = [{empid: 3, name: 'akash', age: 32, joining: "2006-06-20", address: "surat", parent: 2},
            {empid: 4, name: 'sagar', age: 31, joining: "2009-06-20", address: "bangalore", parent: 3},
            {empid: 5, name: 'akashay', age:29, joining: "2010-02-02", address: "gujarat", parent: 4}];

class EmployeeStore {
	@observable empdata = [];
	getAll() {
		console.log('testing all');
	}
}


var store = window.store = new EmployeeStore

export default store