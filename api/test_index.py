import pytest
from api.index import get_session_context

from api.longform_episode_generator import (
    Section,
    ArticleOutline,
    gen_intro,
    gen_outline,
)
from api.models import TranscriptLine


# @pytest.mark.asyncio
# async def test_do_tts():
#     result = await do_tts(line="hello world", voice="Amy")
#     assert result is not None


# @pytest.mark.asyncio
# async def test_generate_audio():
#     transcript = Transcript(
#         transcript_lines=[
#             TranscriptLine(text="hello world", speaker="narrator"),
#             TranscriptLine(text="right back at ya", speaker="allison"),
#         ]
#     )
#     result = await generate_audio(transcript)
#     assert result is not None
#     # assert file audio.mp3 exists
#     assert os.path.exists("audio.mp3")


# @pytest.mark.asyncio
# async def test_do_tts_v2():
#     from index import do_tts_v2

#     result = await do_tts_v2(line="hello world", voice="Amy")
#     assert result is not None


# @pytest.mark.asyncio
# async def test_openai_tts():
#     from index import do_tts_openai

#     result = await do_tts_openai(line="hello world", voice="Amy")
#     assert result is not None


# @pytest.mark.asyncio
# def test_upload_fileobj():
#     from index import upload_fileobj
#     import io

#     result = upload_fileobj(io.BytesIO(b"hello world"), "a-to-p", "episode.mp3")
#     assert result is not None
#     # assert file audio.mp3 exists

article_text = "Several high-profile women in business have recently stepped forward to speak openly and personally about the challenges of balancing work and family in the United States, from Facebook COO Sheryl Sandberg’s blockbuster Lean In to Anne-Marie Slaughter’s much-debated 2012 Atlantic essay about the challenges of “having it all.” Now, a groundbreaking cross-generational Wharton study led by Stewart D. Friedman, founding director of the Wharton Work/Life Integration Project, provides a valuable window into how both men’s and women’s views on work and family have changed over the past 20 years.\nFriedman studied two generations of Wharton college students as they graduated — Gen Xers in 1992 and Millennials in 2012 — about their views on work and family. The study revealed that the number of graduates planning to become parents has dropped precipitously. Friedman’s new book, Baby Bust: New Choices for Men and Women in Work and Family, explores why young people are opting out of parenthood.\nRecently, Jeffrey Klein, executive director of the Wharton Leadership Program, sat down with Friedman to discuss the findings, including the differences in men and women’s views, how organizations and policymakers can contribute to change and where we go from here.\nAn edited transcript of the conversation follows.\nJeffrey Klein: In your new book, Baby Bust, you raise some provocative issues about work and family…. As I read this book, I really felt you were compelled to write it. So, what do you find compelling about this topic?\nStewart D. Friedman: There’s both a personal reason and a professional one. I originally got into this topic area when my first son was born, now 26 years ago. When I met him for the first time, I was overwhelmed by a question that I just couldn’t get out of my head: “What am I going to do to make the world a safe place for him to grow up in?” This is a question that I hadn’t really thought much about before I met him, but I couldn’t stop thinking about it. When I got back into my Wharton classroom about a week later, I framed the question in a slightly different way for the students, the future business leaders of the world: How are you thinking about the development, not so much of talent in the next generation, but of people? What does that mean for you professionally as well as personally, and how are you going to figure out how to do that in your own world?\nThat created quite a stir in the classroom. First of all, they had prepared a case on motivation and reward systems, and I had put that aside for the day. They weren’t very happy about that. But some people were quite upset about the fact that I was talking about family and kids. Others were upset because they didn’t really want to hear about my personal life. But quite a few were really grateful and interested in the questions that I was challenging them with as I just started to rant on this issue, completely unprepared.\nThey turned the question around to me and said, “Well, I don’t know what to do. Why don’t you tell us, since you are the professor?” That began a conversation with students, alumni, business leaders and government officials all over the world that [has lasted] for almost three decades. It started as a very personal question for me, but it very soon became one that I could see was important to my students, our school, our businesses and our society. I began a research program to try to answer some of those questions.\n“What just popped off the screen as we were looking at the initial findings was the result in response to the question, ‘Do you plan to have or adopt children?’” –Stewart Friedman\nKlein: That’s fantastic. I can absolutely relate. I sit across from you as a father myself. You are a father; you have two sons and a daughter. So, this isn’t just an academic exercise.\nFriedman: Definitely not. It is very personal.\nKlein: Who do you hope reads this book? And who might it be difficult for?\nFriedman: One of the things that we started to do with the Wharton Work/Life Integration Project, which we began in 1991, was to survey students and alumni. We [started with] the Class of 1992 undergrads. Almost all of them responded to hundreds of questions about their lives, their careers, their values, their aspirations, their hopes and their dreams. Twenty years later, we asked the same questions of the Class of 2012 and went on to explore what we could discover about how things have changed.\nWhat just popped off the screen as we were looking at the initial findings was the result in response to the question, “Do you plan to have or adopt children?” In 1992, 78% said, “Yes.” In 2012, 42% said, “Yes.”\nKlein: Wow.\nFriedman: I scratched my head and thought, “Can that be right?” And it was. Then the question was, “Why?” The book [explores] why the interest in having children or planning to have children has changed so much and how it’s different for men and for women. The conversation has changed. New voices have entered the conversation. There are new norms evolving among young people and senior people about how to integrate the different parts of life in a way that work. When I first started asking these questions, it was very strange to be a man asking questions about work and family. It was almost all women exploring that question. But being a man at Wharton talking about families and kids, it made me kind of different and strange. I got a lot of attention as a result, just because of who I was, not so much what I was doing in terms of the quality of it. That brought a lot of interest in what we were doing here at Wharton. It’s something that the school was highly supportive of, being in the vanguard of interest in this topic.\nNow, how is it that it’s become difficult for some people to talk about this? I think the most challenged audience would be business leaders and social policy makers because what we observe in the data is that people’s attitudes and values have changed but our social institutions, our government policies and our business practices have not. They are still built around a model of family that has a single earner with a mom at home taking care of the kids. That’s just not the norm anymore. It’s most challenging for those people who have the most responsibility for thinking about the direction of those institutions.\nKlein: You talk about the big decline in the percentage of undergraduate students who want to have children or are sure they are going to have children. Is there a gender difference in that response?\nFriedman: No, it’s exactly the same for men and women: 78% or 79% for men and women in 1992, and then 42% or 43% for men and women in 2012.\nKlein: One of the things that you note is that you are really seeing a change in life priorities among men. Can you describe what that change looks like over these last 20 years?\nFriedman: Men are somewhat more focused on career and a little bit less on family. That’s the general trend there. At the same time, more men who are interested in becoming fathers are interested in being more involved as fathers. They don’t see themselves as the sole bread winner anymore. In 1992, the men in that era were still of a mindset that was pretty traditional. But today’s men, we don’t see that. They expect their spouses to be engaged in careers full time. Men and women also expect to be working a lot more hours. The average number of expected hours per week has gone from 58 hours per week in 1992 to 72 in 2012. That’s 14 hours more per week.\nBut most importantly, young men today expect more conflict between work and family. That’s one of the big inhibitors of their willingness to commit to being parents because they don’t see how they can do it. In addition, to the extent that they carry a lot of student debt, that’s another factor that constrains men in their willingness to think about the prospect of having children. It’s not that they don’t want it — although that has gone down some — it’s, “How do I make it happen in light of all these new pressures?”\nKlein: You talk in the book about students today. I think this applies to both men and women. They don’t expect permanence. They are leaving college and going out into the work world, and they have a different view of career paths.\nFriedman: Yes, they do.\nKlein: Can you describe that a little bit?\nFriedman: That was quite striking. This people of this generation were in their very formative years during [the September 11, 2001 terrorist attacks]. That had a profound impact on them and the Class of 1992. This came through very powerfully in the interviews that we did. But in addition, as has been noted by many people studying the Millennial generation, they are much more mobile, much less committed to organizations. The Class of 2012 entered college as the Great Recession hit. Their sense of insecurity about their economic futures is particularly acute. All those factors lead them to be more interested in moving faster into career tracks that are going to give them security.\nKlein: The next question I would like to ask you is about women. One of the things that really stood out to me was this change in perception among young women as they are leaving college. It used to be considered selfish to want a career, right? Now they feel like it’s selfish to want children. In the conversations that you are having with them, how do they deal with that kind of perception, that kind of sentiment?\nFriedman: One of the pieces of what I see as good news in this story is that more people, women and men, are willing and able to say, “I don’t want to have children.” For women especially, I see this as a kind of social progress in human evolution. In every generation prior to the current one, women have been normatively sanctioned to think of themselves as mothers. There’s almost a mindless march into motherhood throughout history. That question hasn’t really been raised. Today, young women are saying, “I don’t feel a need to do that.”\n“People’s attitudes and values have changed but our social institutions, our government policies and our business practices have not.” –Stewart Friedman\nKlein: So, it’s an opening up of choices in some ways?\nFriedman: Exactly. That’s why the subtitle includes “New Choices.” It’s not just new constraints. There’s good news in this. Now, at the same time there are many men and women who want to have children, but because they don’t have support from their organizations and from our society, they can’t figure out how to make it work. But then there are those who are choosing not to and for good reasons. They don’t want it. I see this as progress that people are able to choose to not become parents because not everybody wants to, nor should everyone become a parent.\nKlein: That’s mirrored, as you note in Baby Bust, by national trends as well, in terms of the average number of births per family and what’s happening within population trends within the country.\nFriedman: Yes, our data reflects the national downward trend in parenthood over the last 20 years.\nKlein: What feels really important to you about changing perceptions for women today versus 20 years ago?\nFriedman: Women seem to be more realistic about what it is going to take to be successful in their lives. They are more interested, according to our study, in friendships, in networks and in being respected in their work and in their lives. They are also more interested in doing work that has positive social value. They want to help others more than the prior generation. One of the striking findings we observed is that the more you wanted to be engaged in providing social value through your work, the less likely it was that you would become a mother.\nIt’s almost as if there’s a competition between serving the family of humanity versus the family that you might create with your own children.\nKlein: For men and for women, what advice do you have to move away from an either/or mentality — either family or career — to one where you can integrate them?\nFriedman: There are a lot of young people who are interested in tackling the question of, “What does it mean for me to be real, to clarify what matters most to me in terms of my values, my vision of the kind of leader I want to become, the kind of world I want to create, to be whole? Who are the most important people in the different parts of my life and what do they really need from me and how can I serve them well?”\n[They are looking at ways] to be innovative, to be continually experimenting with how things get done. I reserve a special section at the end of Baby Bust for … young men, who I find are very confused because we are in a moment in history where things are changing — and changing fast. The models that they grew up with are different from the models that they want to create. The Total Leadership approach [which I teach and is covered in my previous book, Total Leadership] essentially helps you to see what matters most to you and then to figure out how to take creative action that is within your control that helps you to align your actions with your values in a way that serves the people around you that you care about.\nThe experiments that people do to practice and to develop this mindset are in pursuit of what I call “four-way wins” — small actions that you can take that demonstrably improve your work, your home, your community and yourself. By trying to do that in the laboratory of our course, you develop new insights about what’s possible in terms of how to integrate the different parts of your life in a way that works for all of them. By practicing that and seeing what’s possible — usually what people discover is that they have more control and more of a sense of agency and capacity to bring the different parts together — they realize that they can do that as they grow in different parts and different stages of their career.\nKlein: One of the things that you talked about within the book, which also resonates with me as I think about managing boundaries and integrating life, is the double dutch metaphor: You can actually jump two ropes at once. You point to people like Richard Fairbank from Capital One or John Donahoe from eBay. What did you see in their lives and in their careers that could resonate with today’s graduates?\nFriedman: These are two of many, many examples that [shatter] the myth that you have to sacrifice everything in order to be successful in your career. What I have seen time and time and time again in my own life and in the people that I study and work with and consult with is that people are more successful in their careers to the extent that they don’t divest [themselves] of the rest of their lives — their families, their communities, their personal lives, their mind, body and spirit. In fact, they are more successful in their careers to the extent that they invest in those other parts. There’s mutual gain to be had. These two executives are just two of many examples that I’ve been studying and that I’ll be writing about in another book next year.\nBut the common myth there is that you have to give up everything. It’s just not true. Now, that’s not to say that sacrifices aren’t needed and that there’s no pain and disappointment. Of course, we all face that. Because men and women are now more aligned in their views about what it takes to make life work, especially dual-career relationships, we’re seeing a lot more experimentation, a lot more working together — men and women, private and public partnerships — to create models that are different from the ones that you and I grew up with and demonstrate that it doesn’t have to be a zero-sum game. There are different models of career and of family that can work.\nBut it’s a long, slow process. Cultural change is a slog. It takes years and years and years, and it happens in part through the stories that we tell.\nKlein: You said that policymakers and organizational leaders are some of the folks that you hope are reading the book and that they are also the ones responsible for leading this kind of change that you are talking about. In the last chapter of the book, you make recommendations. Could you talk about some of those recommendations? How can organizations start to change to support these kinds of four-way wins and integrated lives?\n“One of the pieces of what I see as good news in this story is that more people, women and men, are willing and able to say, “‘I don’t want to have children.'” –Stewart Friedman\nFriedman: It’s such an important question. For organizational leaders, the key is making flexibility real and using the power of digital communications — technology — to enable real flexibility in terms of where, when and how work gets done. Most importantly, today in 2013, [we should] make heroes of the people who are successful in figuring out new models for how to get work done. That is going to help us overcome the stigma of flexibility, which a number of researchers — Joan Williams, Shelley Correll and others — are writing about and demonstrating is still very, very real for men and for women [who take] flexible work options. It’s stigmatized in most organizations. You have to overcome that by demonstrating that flexibility works. The best way to do that is to tell individual stories of people who are successful in both their work and in the rest of their lives, whatever matters most to them, whether it’s family or social issues or religious — whatever it is. It’s not just about kids.\nThat’s an important function that businesses can play in addition to providing flexible benefits and other kinds of policies. But the real issue is culture and cultural change. Again, the models that are promoted as valued will make it easier for others to see, “If Jeff can do that, maybe I can try that,” as long as it’s going to help the company and me. So, it can’t be just about me and my kids and my needs and my emotional state. It’s what changes can I make that work well for me and for our organization?\nKlein: Stew, you have been at this for more than 20 years. This is obviously a topic that you are deeply connected to, that you are passionate about. Where does it go from here?\nFriedman: One of the things we want to do is to mine the data that we collected about the class of 1992, to learn more about how they have evolved and how they see their futures. Then I’m expecting that in 2032 we’ll survey that class to see what they are thinking and we’ll be doing more ongoing research of Wharton students and alumni to continue to track their values and their interest in the different parts of their lives. What I’m most excited about now is we are launching the Student Advisory Board for the Work/Life Integration Project. We have a couple thousand students at all levels — both MBA and undergrad — who are really eager to help use this research as a platform and as a catalyst for creating a new kind of conversation on our college campus and on other college campuses to invite young men and women to start to talk about what these issues mean for them now. It’s clear that the sooner we engage in real conversation … the much more likely it is that those dreams will be fulfilled because no one’s going to hand it to them. They are going to have to forge it themselves. They are going to need our help. It starts with dialogue informed by research."

article_outline = ArticleOutline(
    title="Balancing Work and Family: Insights from a Wharton Study",
    sections=[
        Section(
            title="Introduction",
            content="Discussion on recent high-profile conversations about work-family balance in the U.S., including contributions from Sheryl Sandberg and Anne-Marie Slaughter. Introduction to Stewart D. Friedman's Wharton study comparing Gen Xers and Millennials' views on work and family.",
            subsections=[],
        ),
        Section(
            title="Study Overview and Key Findings",
            content="Overview of Friedman's study, comparing the perspective of Wharton college students from 1992 and 2012 on work and family. Highlighting the significant decline in graduates planning to become parents and the exploration of this phenomenon in Friedman's book, Baby Bust.",
            subsections=[],
        ),
        Section(
            title="Personal and Professional Motivation Behind the Study",
            content="Friedman discusses his personal and professional reasons for pursuing this area of study, emphasizing the significant impact his son's birth had on his career and research focus.",
            subsections=[],
        ),
        Section(
            title="Shifts in Attitudes Towards Parenthood",
            content="Revelation of changing attitudes towards having children over 20 years, with a dramatic drop in students planning to become or considering becoming parents.",
            subsections=[],
        ),
        Section(
            title="Gender Perspectives and Trends",
            content="Discussion on the changes in men's and women's perspectives on work and family over the past 20 years, including a shift in men's focus towards career over family and a change in women's sentiments towards motherhood.",
            subsections=[
                Section(
                    title="Men's Changing Priorities",
                    content="Details on how men's priorities have shifted towards careers and how their expectations from family life have evolved.",
                    subsections=[],
                ),
                Section(
                    title="Women's Evolving Perceptions",
                    content="Insights into how young women's perceptions about career and motherhood have transformed, moving from viewing career aspirations as selfish to the same sentiment towards wanting children.",
                    subsections=[],
                ),
            ],
        ),
    ],
)

intro_script = [
    TranscriptLine(
        speaker="Jake",
        text="Welcome to ListenArt, where we delve into the intersections of art, culture, and society. I'm Jake.",
    ),
    TranscriptLine(
        speaker="Emily",
        text="And I'm Emily. Today, we're unpacking an intriguing study that throws light on the evolving views of work and family balance in the U.S., an issue that's recently been spotlighted by influential voices like Sheryl Sandberg and Anne-Marie Slaughter.",
    ),
    TranscriptLine(
        speaker="Jake",
        text="Right, Emily. This spotlight is what led to a fascinating cross-generational study conducted by Stewart D. Friedman, who's the founding director of the Wharton Work/Life Integration Project. It offers substantial insights into how views on family and work have shifted between Gen Xers and Millennials.",
    ),
    TranscriptLine(
        speaker="Emily",
        text="Heighlighting a significant change, this study reveals a drastic decline in the number of graduates planning to become parents. It's all explored in Friedman's latest book, Baby Bust: New Choices for Men and Women in Work and Family. But what's really stirring about Friedman's venture into this subject are the personal and professional motivations behind it.",
    ),
    TranscriptLine(
        speaker="Jake",
        text="Absolutely, Emily. It turns out, the birth of Friedman's first son was a turning point for him, sparking a relentless quest to make the world a safer place for his son to grow up in. This personal quest soon translated into a broader question for his students and eventually, a large-scale study comparing perspectives on family and work among Wharton graduates from 1992 and 2012.",
    ),
    TranscriptLine(
        speaker="Emily",
        text="And the findings from this study are pretty groundbreaking. There's been a seismic shift in attitudes towards having kids over the years. The percentage of students planning to become or contemplating parenthood has seen a dramatic drop.",
    ),
    TranscriptLine(
        speaker="Jake",
        text="But it's not just about numbers, Emily. The study also sheds light on changing gender perspectives. On one hand, there's a noted shift towards career prioritization among men. On the other, women's perceptions of motherhood and career aspirations have undergone a transformation too.",
    ),
    TranscriptLine(
        speaker="Emily",
        text="Certainly, Jake. This insight into how young women nowadays view career and motherhood—from once considering career aspirations as selfish to now having a similar sentiment towards wanting children—marks a profound social evolution.",
    ),
    TranscriptLine(
        speaker="Jake",
        text="And with all these shifts and changing attitudes, Friedman's approach to addressing work-family balance is looking at it through the lens of creating new models for integrating life's different aspects, rather than choosing one over the other.",
    ),
    TranscriptLine(
        speaker="Emily",
        text="Absolutely, Jake. It's about opening up new choices and pathways for both men and women to navigate their lives, careers, and familial desires in a more integrated and fulfilling way. It's a deep dive into how visionary studies like Friedman's shape our understanding of societal norms and pressures.",
    ),
    TranscriptLine(
        speaker="Jake",
        text="Right. So, let's start this journey by discussing the major takeaways from Friedman's Wharton study, and explore the impact it has on our views of balancing work and family in today's world.",
    ),
]


def test_get_article_text():
    from api.index import extract_article

    result = extract_article(
        "https://dberkholz.com/2024/01/17/the-lazy-technologists-guide-to-weight-loss/"
    )
    assert result is not None


# @pytest.mark.asyncio
# async def test_generate_episode_longform():
#     article_text = get_article_text("https://thewritetoroam.com/2024/02/how-to-write-stuff-no-one-else-can")
#     result = await generate_episode_longform(article_text)
#     from api.index import generate_audio
#     from api.models import Transcript
#     transcript = Transcript(transcript_lines=result)
#     gen_audio_result = await generate_audio(transcript=transcript, provider=get_tts_provider('openai'), episode_id="test_123")
#     pretty_print(result)
#     print(gen_audio_result)
#     assert result is not None
#     return result


@pytest.mark.asyncio
async def test_intro_generation():
    intro = await gen_intro(outline=article_outline, article_text=article_text)
    assert intro is not None


@pytest.mark.asyncio
async def test_gen_outline():
    outline = await gen_outline(article_text)
    assert outline is not None


# @pytest.mark.asyncio
# async def test_gen_main_sections():
#     script_so_far = intro_script
#     main_sections = await gen_main_sections(article_text=article_text, outline=article_outline, script_so_far=script_so_far)
#     assert main_sections is not None


@pytest.mark.asyncio
async def test_context():
    async with get_session_context() as session:
        session.is_active
