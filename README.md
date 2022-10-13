
<a name="readme-top"></a>

[Contributors][contributors-url]


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-team">About The Team</a>
      <ul>
        <li><a href="#team-role">Team Role</a></li>
        <li><a href="#other-teams-requests-on-team">Other Teams Requests on team</a></li>
      </ul>
    </li>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE TEAM -->
## About The Team (wip)

The Focus of the Test & integration team is to help create an Automated test suite for the different repositories of the Flexicharge project and assist in the construction of regression tests. 

The types of tests that the Test & integration team is to perform are primarily integration test and E2E tests but also assist in the creation of regression tests. Unit tests are at the discretion of the different teams not part of Test & integration. 

### Team Role

The test & integration team role is to make sure the flexicharge system is tested to work and that it functions. As well that the system works as intended. 

### Other Teams Requests on team

Make sure to be in sync with the other teams so that new functionality can be tested at the earliest possible time. The team are also to check the function of the entire business ready system

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ABOUT THE PROJECT -->
## About The Project

FlexiCharge is an upcoming challenger in the electrical car charging industry.
Our vision is to provide the most flexible charging experience in the market.

The test and integration team work towards automating tests for the rest of the project thus ensuring a good quality product.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
The tests are built using Python and PyTest which are deployed through the github actions pipeline on each individual team repository.
The API is accessed with the help of the python module requests


<!--
This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

  [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

- <a href="https://www.docker.com/">Docker</a>

- <a href="https://www.python.org/">Python</a>
- <a href="https://docs.pytest.org">PyTests</a>
- <a href="https://pypi.org/project/requests/">Requests</a>
- <a href="https://github.com/knowitrickard/FlexiCharge-Backend">FlexiCharge Backend</a>
- <a href="https://nodejs.org/en/">Node.js</a>


<!--This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
-->
### Installation
- Run the backend application, same instruction can be found at https://github.com/knowitrickard/FlexiCharge-Backend/blob/main/README.md
1. Get the secrets for the .env file variables. The variables can be found in the .env.example file
2. move into the root directory ```/FlexiCharge-Backend```
3. Build the app with ```docker-compose build```
4. start the program with ```docker-compose up```
- You should now be able to run the tests from the ```/test``` directory 
1. By using ```python pytest /test_*.py``` 


<!--_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


<!--
Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_
-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Test connectivity to rest API.
- [x] Create pipeline using github actions for the forked version of backend repository.
- [x] Implement the working pipeline in the backend repository. 
    - [x] Run the workflow on a branch in the backend repo.
    - [x] Make a <a href="https://github.com/knowitrickard/FlexiCharge-Backend/pull/163">Pull Request</a>
    - [x] Merge branch into main  
- [ ] Use the OCPP endpoints to test the backend app
    - [x] Test manually on local app 
    - [ ] Test in branch on backend repo workflow
    - [ ] Make a pull request
    - [ ] Merge branch into main

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

<!--
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->



<!-- CONTACT -->
## Contact

- Christoffer - 9914kach@gmail.com
- Jesper - peje20le@student.ju.se
- Albin - albin.wiklund11@gmail.com
- Oskar - oskar.s.rundberg@gmail.com
- Iris - irisxinran@gmail.com

Project Link: [https://github.com/users/knowitrickard/projects/2]

All FlexiCharge Repositories: [https://github.com/knowitrickard?tab=repositories]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


<!--
Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)
-->
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/knowitrickard/FlexiCharge-Test-and-integration/graphs/contributors
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
