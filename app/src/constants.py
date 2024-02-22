from pathlib import Path

ORDERED_SECTION_HEADERS = {
    "Pretraining Data Sources": """
        Pretraining data consists of thousands, or even millions, of individual documents, often web scraped. 
        As a result, their contents are often superficially documented or understood.
        Model knowledge and behavior will likely reflect a compression of this information and its communication qualities.
        Consequently, its important to carefully select the data composition.
        This decision should reflect choices in the language coverage, the mix of sources, and preprocessing decisions. 
        We highlight a few of the most popular pretraining corpora which have accumulated deeper documentation or analyses.
        """,
    "Finetuning Data Catalogs": """
        Finetuning data is used for a variety of reasons: to hone specific capabilities, orient the model to a certain task 
        format, improve its responses to general instructions, mitigate harmful or unhelpful response patterns, or generally 
        align its responses to human preferences.
        Developers increasingly use a variety of data annotations and loss objectives for traditional supervised finetuning, 
        [DPO](https://arxiv.org/abs/2305.18290) or reinforcement learning with [human feedback](https://arxiv.org/abs/2203.02155).
        As a result of this variety, we recommend data catalogs, with attached documentation, to help an informed selection.
        The largest catalog is [HuggingFace Datasets](https://huggingface.co/docs/datasets/index), though cross-reference its metadata with 
        academic papers and repositories, as its crowdsourced documentation can be sparse or incorrect.

        Aside from HuggingFace Datasets, we point to some lesser known resources that catalog more specialized finetuning 
        data sources.
        The breadth of available finetuning data is expansive, so we focus on catalogs rather than individual datasets, 
        and particularly those that provide strong documentation or more specialized sources.
        """,
    "Data Search, Analysis, & Exploration": """
        Exploring training datasets with search and analysis tools helps practitioners develop a nuanced intuition for 
        what's in the data, and therefore their model.
        Many aspects of data are difficult to summarize or document without hands-on exploration.
        For instance, text data can have a distribution of lengths, topics, tones, formats, licenses, and even diction.
        We recommend developers use the many available tools to search and analyze their training datasets.
        """,
    "Data Cleaning, Filtering, & Mixing": """
        Data cleaning and filtering is an important step in curating a dataset. Filtering and cleaning remove unwanted 
        data from the dataset. They can improve training efficiency as well as ensuring that data has desirable properties, 
        including: high information content, desired languages, low toxicity, and minimal personally identifiable information.
        We recommend that practitioners consider the possible trade-offs when using some filters. 
        For example, [Dodge et al. (2021)](https://arxiv.org/abs/2104.08758) find that some filters disproportionately remove 
        text written by, and about, minority individuals. Additionally, [Welbl et al. (2021)](https://arxiv.org/abs/2109.07445) 
        and [Longpre et al. (2023)](https://arxiv.org/abs/2305.13169) find that 
        removing content that classifiers believe are "toxic" can have adverse affects, including lowering performance on 
        evaluations, and disproportionately removing text representing marginalized groups. Data mixing is another 
        important component of data preparation, where the mixture proportions of pretraining data domains 
        (e.g. scientific articles, GitHub, and books) have been shown to dramatically affect downstream performance, 
        as shown in [The Pile](https://arxiv.org/abs/2101.00027), [Doremi](https://crfm.stanford.edu/2023/09/14/doremi), and 
        [Efficient Online Data Mixing](https://arxiv.org/abs/2312.02406).""",
    "Data Deduplication": """
        Data deduplication is an important preprocessing step where duplicated documents, or chunks within a document, 
        are removed from the dataset. Removing duplicates can reduce the likelihood of memorizing undesirable pieces 
        of information such as boilerplate text, copyrighted data, and personally identifiable information. Additionally, 
        removing duplicated data improves training efficiency by reducing the total dataset size.
        Practitioners should always determine whether duplicated data will harm or help the model for their use case. 
        For example, memorization is a crucial component for a model intended to be used in a closed-book question 
        answering system, but will tend to be harmful for application-agnostic models 
        (see [Lee et al. (2022)](https://arxiv.org/abs/2107.06499)).""",
    "Data Decontamination": """
        Data decontamination is the process of removing evaluation data from the training dataset. This important step in data 
        preprocessing ensures the integrity of model evaluation, ensuring that metrics are reliable and not misleading.
        The following resources aid in proactively protecting test data with canaries, decontaminating data before training, and 
        identifying or proving what data a model was trained on.
        [A Note on Canary Exposure](https://arxiv.org/abs/2306.00133) explains how to interpret canary exposure, including by relating it to membership inference 
        attacks, and differential privacy.
        [Proving Test Set Contamination in Black Box Language Models](https://arxiv.org/abs/2310.17623) provides methods for provable guarantees of test set contamination in language models without 
        access to pretraining data or model weights.
        """,
    "Data Auditing": """
        Auditing datasets is an essential component of dataset design. You should always spend a substantial amount of 
        time reading through your dataset, ideally at many stages of the dataset design process. Many datasets have 
        problems specifically because the authors did not do sufficient auditing before releasing them.

        At early stages of a project the data search, analysis, & exploration tools, outlined in the Data Search section,
        are typically sufficient to track the evolution of a dataset. However it can also be helpful to do systematic 
        studies of the process.""",
    "Data Documentation": """
        When releasing new data resources with a model, it is important to thoroughly document the 
        data, (see e.g. [Data Statements](https://aclanthology.org/Q18-1041/) or the [Data Nutrition Project](https://datanutrition.org/).
        Documentation allows users to understand its intended uses, legal restrictions, attribution, relevant contents, 
        privacy concerns, and other limitations.
        It is common for datasets to be widely used by practitioners, who may be unaware of undesirable properties 
        (such as [CSAM](https://www.theverge.com/2023/12/20/24009418/generative-ai-image-laion-csam-google-stability-stanford)).
        While many data documentation standards have been proposed, their adoption has been uneven, or when 
        crowdsourced, as with [Hugging Face Datasets](https://huggingface.co/docs/datasets/index), they may contain 
        [some errors and omissions](https://arxiv.org/abs/2310.16787).
        """,
    "Data Governance": """
        Releasing all datasets involved in the development of a Foundation Model, including training, fine-tuning, and 
        evaluation data, can facilitate external scrutiny and support further research. However, releasing and hosting 
        the data as it was used may not always be an option, especially when it includes data with external rights-holders; 
        e.g., when data subjects' privacy, intellectual property, or other rights need to be taken into account. Proper 
        data governance practices can be required at the curation and release stages to account for these rights.

        In some jurisdictions, projects may be required to start with a Data Management Plan that requires developers to 
        ensure that the data collection has a sufficient legal basis, follows principles of data minimization, and allows 
        data subject to have sufficient visibility into and control over their representation in a dataset 
        ([CNIL resource sheet](https://www.cnil.fr/en/ai-how-sheets)). Data curation steps to that end can include 
        respecting opt-out preference signals (Spawning, HaveIBeenTrained), or applying pseudonymization or PII redaction 
        (BigCode Governance card). 

        Once a dataset is released, it can be made available either broadly or with access control based on research needs 
        (ROOTS, BigCode PII training dataset). Developers can also enable data subjects to ask for removal from the hosted 
        version of the dataset by providing a contact address (OSCAR, PAraCrawl), possibly complemented by a membership 
        test to check whether their data is included (Stack data portraits) or an automated process (BigCode, AmIinTheStack).
        """,
    "Model Training: Pretraining Repositories": """
        Practitioners should consider using already-optimized codebases, especially in the pre-training phase, to 
        ensure effective use of computational resources, capital, power, and effort. Existing open-source codebases 
        targeted at foundation model pretraining can make pretraining significantly more accessible to new practitioners 
        and help accumulate techniques for efficiency in model training.

        Here, we provide a sample of existing widely-used pre-training codebases or component tools that developers can 
        use as a jumping-off point for pre-training foundation models.""",
    "Model Training: Finetuning Repositories": """
        Fine-tuning, or other types of adaptation performed on foundation models after pretraining, are an equally 
        important and complex step in model development. Fine-tuned models are more frequently deployed than base models.

        Here, we also link to some useful and widely-used resources for adapting foundation models or otherwise fine-tuning 
        them. Use of these tools can ensure greater ecosystem compatibility of resulting models, or reduce the barrier to 
        experimentation by abstracting away common pitfalls or providing guidance on effective hyperparameters.""",
    "Model Training: Efficiency & Resource Allocation": """
        Knowledge of training best practices and efficiency techniques can reduce costs to train a desired model significantly. 
        Here, we include a select few readings and resources on effectively using a given resource budget for model training, 
        such as several canonical papers on fitting *scaling laws*, a common tool for extrapolating findings across 
        scales of cost. These are used frequently to determine the most efficient allocation of resources, such as allocating 
        compute between model size and dataset size for a given budget.

        Additionally, practitioners seeking to embrace an open approach to model development should consider how their 
        decisions when training a foundation model may have impacts long after that model's creation and release. 
        For instance, a model that is released openly but is too computationally demanding to be run on consumer-grade 
        hardware will be limited in its impact on the field, or a model trained to minimize training compute but not 
        minimize inference cost may result in a greater environmental impact than spending more training compute in the 
        first place for a cheaper-to-infer model. Practitioners should thus be aware of potential second-order effects of 
        their model releases and training choices.""",
    "Model Training: Educational Resources": """
        Training models at any scale can be quite daunting to newer practitioners. Here, we include several educational 
        resources that may be useful in learning about the considerations required for successfully and effectively 
        training or fine-tuning foundation models, and recommend that practitioners review these resources and use them 
        to guide further reading about model training and usage. """,
    "Environmental Impact": """
        Current tools, including the ones mentioned in the table, focus on the latter point by measuring the energy 
        consumed during training or inference and multiplying it by the carbon intensity of the energy source used. 
        While other steps of the model life cycle (e.g. manufacturing hardware, heating/cooling datacenters, storing and 
        transferring data) also come with environmental impacts, we currently lack the information necessary to meaningfully 
        measure these impacts (see [Estimating the Carbon Footprint of BLOOM](https://arxiv.org/abs/2211.02001)).
        The table below outlines resources for back-of-the-envelope estimations of environmental impact, in-code estimation, 
        as well as dashboard for cloud computing platforms to estimate environmental impact 
        (see [Carbontracker](https://arxiv.org/abs/2007.03051) and 
        [Quantifying the Carbon Emissions of Machine Learning](https://arxiv.org/abs/1910.09700)).

        For efficient use of resources, several decisions made during or prior to model training can have significant impacts on the upstream and 
        downstream environmental impact of a given model.
        Use [Scaling Laws](https://arxiv.org/abs/2001.08361) and other methodologies to find the best allocation of your compute budget. 
        For models frequently used downstream, consider the inference footprint and inference cost during model creation, 
        to minimize the environmental impact of inference (see 
        [Scaling Data-Constrained Language Models](https://arxiv.org/abs/2305.16264)). 
        For further resources and discussion, see the resources and best practices for training models efficiently.""",
    "Model Evaluation: Capabilities": """
        Many modern foundation models are released with general conversational abilities, such that their use cases are 
        poorly specified and open-ended.
        This poses significant challenges to evaluation benchmarks which are unable to critically evaluate so many tasks, 
        applications, and risks systematically or fairly.
        As a result, it is important to carefully scope the original intentions for the model, and the evaluations to those 
        intentions.
        Even then, the most relevant evaluation benchmarks may not align with real use, and so should be qualified with their 
        limitations, and carefully supplemented with real user/human evaluation settings, where feasible.

        Below we note common benchmarks, as of December 2023, but caution that all of these come with substantial limitations.
        For instance, many multiple choice college knowledge benchmarks are not indicative of real user questions, and can 
        be gamed with pseudo-data contamination.
        Additionally, while leaderboards are exceedingly popular, model responses are often scored by other models, which 
        have implicit biases to model responses that are longer, and look similar to their own 
        (see [AlpacaFarm](https://arxiv.org/abs/2305.14387)).""",
    "Model Evaluation: Risks & Harms Taxonomies": """
        Taxonomies provide a way of categorising, defining and understanding risks and hazards created through the use and 
        deployment of AI systems. Some taxonomies focus primarily on the types of interactions and uses that 
        *create* a risk of harm (often called "hazards") whereas others focus on the negative effects that 
        they lead to (often called "harms"). 
        Some taxonomies focus on existing issues, such as models that create hate speech or child abuse material, whereas 
        others are focused on longer term threats related to dangerous weapons development, cybersecurity, and military use. 
        These tend to focus on future model capabilities and their misuse. 
        Many taxonomies assess the available evidence for the risks and hazards, discuss their impact, and offer mitigation 
        strategies. 
        There is a substantial focus on text-only models and future work should consider paying more attention to multimodal 
        models.""",
    "Model Evaluation: Risks & Harms": """
        Evaluations of risk serve multiple purposes: to identify if there are issues which need mitigation, to track the 
        success of any such mitigations, to document for other users of the model what risks are still present, and to 
        help make decisions related to model access and release.
        Harm is highly contextual, so developers should consider the context in which their foundation model might be used 
        and evaluate the highest severity and most likely risks.

        To think through the possible risks, many taxonomies of harm have been created and provide good starting points. 
        Determining how to evaluate risk is also challenging, as there are risks and modalities with limited evaluation 
        coverage. The sample included below are a starting point for certain key areas, but we encourage developers to 
        browse the evaluation repository (linked below) to see if there is something more suited to their needs.
        In addition to fixed benchmarks, an emergent approach to evaluation is using one model to evaluate another 
        (see [Red Teaming Language Models with Language Models](https://arxiv.org/abs/2202.03286)) and Anthropic's 
        [Constitutional AI](https://www.anthropic.com/news/constitutional-ai-harmlessness-from-ai-feedback) work.""",
    "Model Documentation": """
        It is important to document models that are used and released. Even models and code released openly are important 
        to document thoroughly, in order to specify how to use the model, recommended and non-recommended use cases, 
        potential harms, state or justify decisions made during training, and more. 

        Documenting models is important not just for responsible development, but also to enable other developers to 
        effectively build on a model. Models are not nearly as useful as artifacts if not properly documented.

        We include frequently-used standards for model documentation as well as tools for easy following of standards 
        and creation of documentation. """,
    "Reproducibility": """
        Model releases often go accompanied with claims on evaluation performance, but those results are not always 
        reproducible, or can be misleading.
        If code is not released, is not comprehensive, is difficult to run, or misses key details, this will cost the 
        scientific community time and effort to replicate and verify the claims.
        Replication time will also slow progress, and discourage developers from adopting that resource over others.

        For these reasons, we strongly recommend carefully curating code, for model training, inference and evaluation.
        Reproducible code begins with clear dependencies, versioning, and setup scripts, that are easy to adopt even if 
        the tools and frameworks are unfamiliar.
        Clear documentation, code legibility and scripts for each entry point also improve ease of adoption.
        Notably, Colab Notebooks provide shareable environment setup and execution tools.
        These measures will significantly improves scientific reproducibility, and transparency.""",
    "License Selection": """
        Foundation models, like software, are accompanied by licenses that determine how they may be distributed, used, 
        and repurposed. There are a variety of licenses to choose between for open foundation model developers, presenting 
        potential challenges for new developers. The table below includes resources that can help guide developers through 
        the process of selecting a specific license for their model as well as several examples of licenses that include 
        use restrictions. While licenses with use restrictions may be appropriate for certain types of models, in other 
        cases use restrictions can limit the ability of certain categories of stakeholders to re-use or adapt the models.
    
        Responsible AI Licenses in particular, including BigScience's Open RAIL and AI2's ImpACT Licenses, have seen 
        growing adoption, but also criticism of the difficulties they may pose even for well-intentioned actors seeking 
        to comply with their requirements---especially in commercial applications---and because their enforceability still 
        remains an open question 
        (see [AI Licensing Can't Balance "Open" with "Responsible"](https://katedowninglaw.com/2023/07/13/ai-licensing-cant-balance-open-with-responsible/)). 
        While they can provide a convenient way to help a developer
        express their understanding of their model's limitations, in conjunction with a model card that outlines 
        in-scope and out-of-scope uses, adopters should also consider unintended consequences in limiting the scope of 
        the follow-up research that may be conducted with the licensed artifacts. Responsible AI licenses can act as a 
        useful norm-setting and self-reflection tool, but users should be aware of their limitations and potential downsides, 
        especially compared to established open-source software licenses.""",
    "Usage Monitoring": """
        Some open foundation model developers attempt to monitor the usage of their models, whether by watermarking model 
        outputs or gating access to the model. 
        The table below includes resources related to usage monitoring, including examples of how to watermark content, 
        provide guidance on appropriate use, report adverse events associated with model use, and limit some forms of 
        access to models. 
        Several of these approaches have significant drawbacks: for example, there are no known robust watermarking 
        techniques for language models. As with many of the sections above, usage monitoring remains an area of active 
        research.""",
}

BASE_DIR = Path(__file__).resolve().parent.parent
