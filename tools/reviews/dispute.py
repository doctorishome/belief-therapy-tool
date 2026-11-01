"""Adds 'possible cognitive errors' and 'questions to dispute the belief' under Challenge (clinical).

Error definitions come word for word from the Belief Counseling Cognitive Errors Checklist.
Questions come word for word from the Questioning False Beliefs form (questioning_form.json),
referenced by number so the wording can never drift from the form.
"""
import json, os
from dispute_data import DATA

CHECKLIST = 'https://doctorishome.github.io/belief-therapy-tool/counselors/forms/Belief-Counseling-Cognitive-Errors-Checklist.pdf'
FORM = 'https://doctorishome.github.io/belief-therapy-tool/counselors/forms/Belief-Counseling-Questioning-False-Beliefs.pdf'

DEF = {
    'Selective attention': 'noticing only what fits my belief',
    'Confirmatory bias': 'looking for proof I’m right, ignoring the rest',
    'Mental filter': 'dwelling on the one negative',
    'Disqualifying the positive': 'deciding good things don’t count',
    'All-or-nothing thinking': 'no middle ground',
    'Overgeneralization': 'one event becomes a rule',
    'Catastrophizing': 'expecting the worst possible outcome',
    'Minimization': 'shrinking my strengths or successes',
    'Mind reading': 'assuming I know what others think',
    'Fortune telling': 'predicting a bad outcome',
    'Jumping to conclusions': 'deciding without the facts',
    'Emotional reasoning': 'I feel it, so it must be true',
    'Global labeling': 'one mistake becomes who I am',
    'Personalization': 'taking blame for things outside my control',
    'Blaming others': 'others are responsible for how I feel',
    'Hindsight bias': 'I should have seen it coming',
    'Should statements': 'rigid musts and oughts',
    'Perfectionism': 'standards no one could meet',
    'Comparisons': 'measuring myself against others',
    'Unrealistic expectations': 'expecting too much of myself or others',
    'Helplessness': 'outside forces control everything',
    'Over-responsibility': 'I must control every outcome',
    'Underestimating myself': 'doubting I can cope',
    'Avoidance': 'pushing away painful thoughts',
}

_f = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questioning_form.json')))
Q = _f['spiritual'] + _f['general']


def add_dispute(body, key):
    d = DATA[key]
    i = next(n for n, (k, t) in enumerate(body) if k == 'B' and t.startswith('**Challenge (clinical).**'))
    who = d.get('who', '')
    body[i] = ('B', body[i][1] + f' **Possible cognitive errors** to watch for{who}, with their definitions from the '
               f'[Belief Counseling Cognitive Errors Checklist]({CHECKLIST}) and the {d.get("label", "symptoms")} they tend to feed:')
    add = []
    for e in d['errors']:
        name, feeds, sounds = e[:3]
        assert name in DEF, name
        t = f'**{name}** — {DEF[name]}. *Feeds:* {feeds}. *Sounds like:* “{sounds}”'
        if len(e) > 3:
            t += ' ' + e[3]
        add.append(('B2', t))
    intro = d.get('qintro', 'Have the client choose questions from the [Questioning False Beliefs]({form}) form that “speak to” the belief.')
    video = ' To see how, watch Dr. Campbell’s video [Integrated Christian Counseling: Questioning Your Beliefs](https://www.youtube.com/watch?v=ZjR0Mx1zEMY).'
    add.append(('B', '**Questions to dispute the belief.** ' + intro.format(form=FORM) + video + ' Selected questions that fit the errors above:'))
    for nums, target in d['questions']:
        nums = nums if isinstance(nums, tuple) else (nums,)
        add.append(('B2', ' and '.join(f'“{Q[n]}”' for n in nums) + f' *For:* {target}.'))
    return body[:i + 1] + add + body[i + 1:]
