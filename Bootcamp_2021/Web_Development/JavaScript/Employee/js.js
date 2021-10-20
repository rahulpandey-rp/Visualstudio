const employee = [
	{ name: 'Naman Mathur', age: 24, salary: 2000, dob: '10/5/1996'},
	{ name: 'Tanmay Singh', age: 23, salary: 8000, dob: '8/3/1997'},
	{ name: 'Ajey Nagar', age: 22, salary: 3000, dob: '3/6/1995'},
	{ name: 'Aman Jain', age: 20, salary: 9000, dob: '23/1/2001'},
	{ name: 'Peter Parker', age: 28, salary: 500, dob: '15/2/1992'},
	{ name: 'D.James', age: 26, salary: 800, dob: '11/9/1994'}
];
const checkSal = employee.filter((sal) => {
	return sal.salary > 5000;
});
console.log(checkSal);
function groupBy(key){
	return function group(array){                  
		return array.reduce((acc,obj) => {
			const prop = obj[key];
			acc[prop] = acc[prop] || [];
			acc[prop].push(obj);
			return acc
		}, {});
	};
}
const groupByAge = groupBy('age');
console.log(groupByAge(employee));
const fetchEmp = employee.filter((fetch) => {
	return fetch.salary < 1000 && fetch.age > 20;
});
console.log(fetchEmp);
const sal_Inc1 = fetchEmp[0].salary * 5;
const sal_Inc2 = fetchEmp[1].salary * 5;
console.log(sal_Inc1, sal_Inc2);