# PostCSS

CSS files that are inside `static/styles` needs PostCSS, otherwise the syntax of it may be not recognized by browsers.
To install PostCSS you need **node** and **npm**.

I choose **yarn** as my package manager, so if you're using an alternate package manager such as **npm**, **bower**, or **pnpm**, you should remove the lockfile and run the install command (**npm i** for npm & **pnpm install** for pnpm).

### Yarn
Type `yarn` on your terminal and enter, then it will install all dependencies listed in **package.json**.

After installation, type `yarn dev` to start both Flask and PostCSS, or you can enable them individually. `yarn flask` to run Flask, and `yarn postcss` to run PostCSS.

### npm
Type `npm i` on your terminal  and enter, then it will install all dependencies listed in **package.json**.

After installation, edit the **package.json** file first.
![](./img/scripts.png)
In this image above, as you can see all the scripts inside **package.json**.

Renaming: <br>
`\"yarn:start:*\"` &rarr; `\"npm:start:*\"`

`"flask": "yarn start:flask"` &rarr; `"flask": "npm run start:flask"`

`"postcss": "yarn start:postcss"` &rarr; `"postcss": "npm run start:postcss"`

After renaming, type `npm run dev` to start both Flask and PostCSS, or you can enable them individually. `npm run flask` to run Flask, and `npm run postcss` to run PostCSS.