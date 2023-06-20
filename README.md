# PulsarWave


The Automated Trend Monitoring Radar (TMR), PulsarWave, is an innovative technology that uses advanced Machine Learning (ML) algorithms to sift through, evaluate, and draw insights from a sea of data amassed from news feeds. This sophisticated tool stands on the principle of a posteriori knowledge, creating new insights through the processing and analysis of empirical data. It utilizes Natural Language Processing (NLP), a pivotal subset of artificial intelligence, to parse and understand text-based data, thereby identifying and following emerging trends in the rapidly changing world of digital media.

What sets TMR apart from typical "social listening" tools is its ability to prioritize the importance and relevance of emerging news, focusing on the quality of information rather than just its popularity or frequency of mention. Instead of merely detecting what's "trending", TMR aims to highlight substantial news items that indicate a real shift or development in the current landscape, be it political, social, or economic. Companies can leverage it to monitor sentiment and foresee market trends, enhancing their strategic planning and decision-making processes. In public health, it could be instrumental in early disease detection or tracking health trends based on reported experiences. Policymakers can harness it to understand public sentiment around key issues, making informed decisions that truly reflect the needs of their constituents. Furthermore, TMR could play a critical role in combating disinformation by identifying and prioritizing factual, significant news over popular yet potentially misleading information. Through its advanced capabilities, the Automated Trend Monitoring Radar doesn't just echo the digital world's noise—it carefully selects and amplifies the most meaningful signals, making it an invaluable tool for a wide array of real-world applications.  

The Trend Monitoring Radar has been modified from Zalando's [public Tech Radar](http://zalando.github.io/tech-radar/)

**Note please revise your own API_KEY**

## How to use

1\. Export your [OpenAI API key](https://platform.openai.com/account/api-keys) as `OPENAI_API_KEY` and related tweeter API keys in run_ai_process.sh. Please monitor crontab.txt to observe the sequence of the process.

```console
$ cd src
$ export OPENAI_API_KEY=YOUR_API_KEY
```

2\. Install the lastest version of the `openai` python package
```console
$ pip install --upgrade openai
```

3\. Run the script, and check the results. And then form the output file, you can run the tech-radar/docs/generate_tech_radar.sh

```console
$ ./run_ai_process.sh
$ ./weekly_pestle_summary.sh 
$ cd ../tech-radar/docs
$ cp ../src/revised_accu_process_tweet.txt ./entry.txt
$ ./generate_tech_radar.sh
```

4\. Start Trend Radar

```console
$ cd ..
$ yarn start
```