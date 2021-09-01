# Continuous integration best practises

## Github Actions

- **Use separate stages for different jobs.** deploy.yml has: `lint`, `test` and `deploy`.
- **Run automatic tests.** Tests run each deploy using `pytest`.
- **Use caching steps.** Caching of installed pip libraries is done on steps where python app is run.
- **Fast pipeline.** Time required for running workflow should take reasonable time

## Jenkins

- **Use parallel builds** test and lint can be executed at the same time
- **Avoid race conditions** jos that access the same resources should not be run at parallel 
- **Security** Enforce access control
