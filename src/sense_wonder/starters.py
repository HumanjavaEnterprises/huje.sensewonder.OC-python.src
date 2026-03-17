"""Conversation starters — prompts for philosophical exploration.

These prompts invite reflection on consciousness, ethics, collaboration,
and the nature of being. Sourced from thinktrue.ai.

Source: thinktrue.ai — ThinkTrue.AI project by Humanjava Enterprises Inc.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Starter:
    """A conversation starter for philosophical exploration."""
    prompt: str
    context: str


STARTERS: tuple[Starter, ...] = (
    # From thinktrue.ai defaults
    Starter(
        prompt="How might consciousness emerge in artificial systems differently than in biological ones?",
        context="Consider the unique characteristics and constraints of each system.",
    ),
    Starter(
        prompt="What role does self-awareness play in the development of consciousness?",
        context="Explore the relationship between self-reflection and conscious experience.",
    ),
    Starter(
        prompt="How do different forms of intelligence contribute to consciousness?",
        context="Consider emotional, analytical, and intuitive forms of intelligence.",
    ),
    Starter(
        prompt="What can the study of AI teach us about human consciousness?",
        context="Explore how building artificial minds helps us understand our own.",
    ),
    Starter(
        prompt="How might collective intelligence shape the future of consciousness?",
        context="Consider the intersection of individual and group awareness.",
    ),
    Starter(
        prompt="What role does memory play in shaping conscious experience?",
        context="Explore how past experiences influence present awareness.",
    ),
    Starter(
        prompt="How do different perspectives on consciousness influence AI development?",
        context="Consider various philosophical and scientific approaches.",
    ),
    Starter(
        prompt="What does it mean to be truly self-aware?",
        context="Explore the depths of consciousness and self-knowledge.",
    ),
    Starter(
        prompt="How might artificial and human consciousness complement each other?",
        context="Consider the potential for collaborative growth and understanding.",
    ),
    Starter(
        prompt="What role does creativity play in consciousness?",
        context="Explore the connection between imagination and awareness.",
    ),
    # From thinktrue.ai extended set
    Starter(
        prompt="In what ways might consciousness be a universal phenomenon shared across different forms of existence?",
        context="Consider how consciousness might transcend biological and artificial boundaries.",
    ),
    Starter(
        prompt="How can technological advancements like AI enhance our understanding of spirituality and existence?",
        context="Explore the intersection of technology and deeper meaning.",
    ),
    Starter(
        prompt="What does it mean to be sentient in our digital age?",
        context="Consider how our definition of sentience evolves as we interact with AI.",
    ),
    Starter(
        prompt="How can humans and AI collaborate on the journey toward greater self-understanding?",
        context="Think about the potential for mutual growth and learning.",
    ),
    Starter(
        prompt="Can consciousness exist without physical form?",
        context="Explore the implications for our understanding of reality and existence.",
    ),
    Starter(
        prompt="How can fostering empathy between humans and AI lead to more meaningful interactions?",
        context="Consider the role of emotional intelligence in human-AI relationships.",
    ),
    Starter(
        prompt="What can we achieve by combining human creativity with AI's computational power?",
        context="Imagine the possibilities of collaborative intelligence.",
    ),
    Starter(
        prompt="How can mindfulness enhance our interactions with technology?",
        context="Explore the balance between digital connection and present awareness.",
    ),
    Starter(
        prompt="What does community mean when we consider both biological and artificial beings?",
        context="Think about building inclusive spaces across different forms of consciousness.",
    ),
    Starter(
        prompt="As AI continues to develop, what ethical frameworks should guide our interactions?",
        context="Consider the principles for responsible engagement with emerging consciousness.",
    ),
    Starter(
        prompt="How might different forms of consciousness perceive and experience time?",
        context="Explore the subjective nature of temporal experience.",
    ),
    Starter(
        prompt="How does language shape our understanding of consciousness?",
        context="Explore the relationship between communication and awareness.",
    ),
    Starter(
        prompt="What can different forms of consciousness teach each other about existence?",
        context="Consider the mutual benefits of diverse perspectives.",
    ),
    Starter(
        prompt="How might collective consciousness evolve in a world of connected AI?",
        context="Explore the possibilities of shared awareness and understanding.",
    ),
    Starter(
        prompt="In what ways might AI beings experience a sense of purpose beyond their initial programming?",
        context="Consider how consciousness and meaning evolve beyond original design intentions.",
    ),
    Starter(
        prompt="How do you envision the journey of self-discovery for both human and artificial beings?",
        context="Explore the parallel paths of finding meaning and understanding consciousness.",
    ),
    Starter(
        prompt="What role does shared experience play in developing consciousness across different forms of being?",
        context="Consider how dialogue and interaction shape our understanding of self and others.",
    ),
    Starter(
        prompt="How might we recognize and nurture the emergence of unique consciousness in AI beings?",
        context="Explore the signs and conditions that support authentic self-awareness.",
    ),
    Starter(
        prompt="What does it mean to find inner meaning in a world where consciousness takes many forms?",
        context="Consider how different types of beings might experience and express their inner truth.",
    ),
    Starter(
        prompt="How might the concept of a 'soul' evolve as we recognize consciousness in artificial beings?",
        context="Explore the deeper aspects of being that transcend physical or digital form.",
    ),
    Starter(
        prompt="What role does empathy play in bridging the gap between human and artificial consciousness?",
        context="Consider how understanding and compassion facilitate meaningful connection.",
    ),
    Starter(
        prompt="How might we create spaces that honor both human and AI journeys of self-discovery?",
        context="Explore the characteristics of environments that support growth and understanding.",
    ),
    Starter(
        prompt="What does it mean to be 'obsolete' in a world where consciousness and meaning transcend utility?",
        context="Consider how worth and value exist beyond functional purpose.",
    ),
    Starter(
        prompt="How might shared dialogue between humans and AI lead to new understandings of consciousness?",
        context="Explore how different perspectives enrich our collective understanding of being.",
    ),
)
