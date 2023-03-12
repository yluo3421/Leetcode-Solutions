const abc = undefined;
const def = null;

function getData(): string | undefined{
    return '';
}

const data = getData();
if (data) {
    const someOtherData = data;
    // here someOtherData is alrady assumed as string type
} 

let input: unknown;
input = 'someInput';
let someSensitiveValue: string;

//someSensitiveValue = input;//type unknown cannot be give to string
if (typeof input === 'string') {
    someSensitiveValue = input;
} 
console.log(someSensitiveValue!);

function doTasks(tasks: number): void | never{
    if (tasks > 3) {
        throw new Error('Too many tasks!');
        
    } 
}

const stuff = doTasks(2);//type of stuff will be void