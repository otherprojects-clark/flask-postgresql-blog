import { type } from 'os'
import { spawn } from 'child_process'

let ostype = type()
let py;

if (ostype == 'Windows_NT'){
  py = spawn("py", ['app.py'])
} else {
  py = spawn("python3", ['app.py'])
}

py.stdout.on('data', (data) => {
  console.log(`${data}`)
})

py.stderr.on('data', (data) => {
  console.error(`${data}`);
});
